from urbanstats.geometry.shapefiles.shapefile import Shapefile
from urbanstats.geometry.shapefiles.shapefiles.judicial import render_start_and_end

HISTORICAL_CONGRESSIONAL = Shapefile(
    hash_key="historical_congressional_5",
    path="named_region_shapefiles/congressional_districts/combo/historical.pkl",
    shortname_extractor=lambda x: f'{x["state"]}-{int(x["district"]):02d} [{render_start_and_end(x)} Congress]',
    longname_extractor=lambda x: f"Historical Congressional District"
    + f" {x['state']}-{x['district']}, {render_start_and_end(x)} Congress, USA",
    filter=lambda x: True,
    meta=dict(
        type="Historical Congressional District",
        source="Census",
        type_category="Political",
    ),
    chunk_size=100,
)
