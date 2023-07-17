import json
import re

import numpy as np
import pandas as pd

from census_blocks import RADII
from stats_for_shapefile import (
    racial_statistics,
    housing_stats,
    education_stats,
    generation_stats,
    income_stats,
    transportation_stats,
)
from election_data import vest_elections
from relationship import ordering_idx


def create_page_json(
    folder,
    row,
    relationships,
    long_to_short,
    long_to_population,
    long_to_type,
):
    statistic_names = get_statistic_names()
    data = dict(
        shortname=row.shortname,
        longname=row.longname,
        source=row.source,
        article_type=row.type,
        rows=[],
    )

    for stat in statistic_names:
        row_text = dict(
            statname=statistic_names[stat],
            statval=float(row[stat]),
            ordinal=0 if np.isnan(row[stat, "ordinal"]) else int(row[stat, "ordinal"]),
            overall_ordinal=0 if np.isnan(row[stat, "overall_ordinal"]) else int(row[stat, "overall_ordinal"]),
            percentile_by_population=float(row[stat, "percentile_by_population"]),
        )
        data["rows"].append(row_text)
    to_add = {}
    for relationship_type in relationships:
        for_this = relationships[relationship_type].get(row.longname, set())
        for_this = [x for x in for_this if x in long_to_population]
        for_this = sorted(
            for_this, key=lambda x: order_key_for_relatioships(x, long_to_type[x])
        )
        for_this = [
            dict(longname=x, shortname=long_to_short[x], row_type=long_to_type[x])
            for x in for_this
        ]
        to_add[relationship_type] = for_this
    data["related"] = to_add

    name = create_filename(row.longname)
    with open(f"{folder}/{name}", "w") as f:
        json.dump(data, f)
    return name


def order_key_for_relatioships(longname, typ):
    processed_longname = longname
    if typ == "Historical Congressional District":
        parsed = re.match(r".*[^\d](\d+)[^\d]*Congress", longname)
        end_congress = int(parsed.group(1))
        processed_longname = -end_congress, longname
    return ordering_idx[typ], processed_longname


def create_filename(x):
    x = x.replace("/", " slash ")
    return f"{x}.json"


def compute_ordinals_and_percentiles(
    frame, key_column, population_column, stable_sort_column, *, just_ordinal
):
    key_column_name = key_column
    ordering = (
        frame[[stable_sort_column, key_column_name]]
        .fillna(-float("inf"))
        .sort_values(stable_sort_column)
        .sort_values(key_column_name, ascending=False, kind="stable")
        .index
    )
    # ordinals: index -> ordinal
    ordinals = np.array(
        pd.Series(np.arange(1, frame.shape[0] + 1), index=ordering)[frame.index]
    )
    if just_ordinal:
        return ordinals, None
    total_pop = frame[population_column].sum()
    # arranged_pop: ordinal - 1 -> population
    arranged_pop = np.array(frame[population_column][ordering])
    # cum_pop: ordinal - 1 -> population of all prior
    cum_pop = np.cumsum(arranged_pop)
    # percentiles_by_population: index -> percentile
    percentiles_by_population = 1 - cum_pop[ordinals - 1] / total_pop
    return ordinals, percentiles_by_population


def add_ordinals(frame, *, overall_ordinal):
    keys = get_statistic_names()
    assert len(set(keys)) == len(keys)
    frame = frame.copy()
    frame = frame.reset_index(drop=True)
    for k in keys:
        ordinals, percentiles_by_population = compute_ordinals_and_percentiles(
            frame, k, "population", "longname", just_ordinal=overall_ordinal
        )
        frame[k, "overall_ordinal" if overall_ordinal else "ordinal"] = ordinals
        if overall_ordinal:
            continue
        frame[k, "total"] = frame[k].shape[0]
        frame[k, "percentile_by_population"] = percentiles_by_population
    return frame


def format_radius(x):
    if x < 1:
        return f"{x * 1000:.0f}m"
    else:
        assert x == int(x)
        return f"{x:.0f}km"


def get_statistic_names():
    ad = {f"ad_{k}": f"PW Density (r={format_radius(k)})" for k in RADII}
    return {
        "population": "Population",
        **{"ad_1": ad["ad_1"]},
        "sd": "AW Density",
        **racial_statistics,
        **education_stats,
        **generation_stats,
        **income_stats,
        **housing_stats,
        **transportation_stats,
        **{(elect.name, "margin"): elect.name for elect in vest_elections},
        **{k: ad[k] for k in ad if k != "ad_1"},
    }


def get_statistic_categories():
    ad = {f"ad_{k}": f"other_densities" for k in RADII}
    result = {
        "population": "main",
        **{"ad_1": "main"},
        "sd": "main",
        **{k: "race" for k in racial_statistics},
        **{k: "education" for k in education_stats},
        **{k: "generation" for k in generation_stats},
        **{k: "income" for k in income_stats},
        **{k: "housing" for k in housing_stats},
        **{k: "transportation" for k in transportation_stats},
        **{(elect.name, "margin"): "election" for elect in vest_elections},
        **{k: ad[k] for k in ad if k != "ad_1"},
    }
    return result


category_metadata = {
    "main": dict(name="Main", show_checkbox=False, default=True),
    "race": dict(name="Race", show_checkbox=True, default=True),
    "education": dict(name="Education", show_checkbox=True, default=False),
    "generation": dict(name="Generation", show_checkbox=True, default=False),
    "income": dict(name="Income", show_checkbox=True, default=False),
    "housing": dict(name="Housing", show_checkbox=True, default=False),
    "transportation": dict(name="Transportation", show_checkbox=True, default=False),
    "election": dict(name="Election", show_checkbox=True, default=True),
    "other_densities": dict(
        name="Other Density Metrics", show_checkbox=True, default=False
    ),
}
