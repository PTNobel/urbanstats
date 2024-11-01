from abc import ABC, abstractmethod

from urbanstats.acs.load import aggregated_acs_data, aggregated_acs_data_us_pr

ORDER_CATEGORY_MAIN = 0
ORDER_CATEGORY_OTHER_DENSITIES = 1


class StatisticCollection(ABC):
    def __init__(self):
        quiz_overlaps = set(self.quiz_question_unused()) & set(
            self.quiz_question_names()
        )
        assert (
            not quiz_overlaps
        ), f"Quiz questions both used and unused: {quiz_overlaps}"
        quiz_questions = set(self.quiz_question_names()) | set(
            self.quiz_question_unused()
        )
        all_columns = set(self.name_for_each_statistic())
        extra_quiz_questions = quiz_questions - all_columns
        assert not extra_quiz_questions, f"Extra quiz questions: {extra_quiz_questions}"
        missing_quiz_questions = all_columns - quiz_questions
        assert (
            not missing_quiz_questions
        ), f"Missing quiz questions: {missing_quiz_questions}"

    @abstractmethod
    def name_for_each_statistic(self):
        pass

    @abstractmethod
    def explanation_page_for_each_statistic(self):
        pass

    @abstractmethod
    def quiz_question_names(self):
        pass

    def quiz_question_unused(self):
        return ()

    @abstractmethod
    def compute_statistics(self, shapefile, statistics_table, shapefile_table):
        pass

    @abstractmethod
    def for_america(self):
        pass

    @abstractmethod
    def for_international(self):
        pass

    def same_for_each_name(self, value):
        return {name: value for name in self.name_for_each_statistic()}

    def extra_stats(self):
        return {}

    def __permacache_hash__(self):
        return (self.__class__.__name__, getattr(self, "version", None))


class GeographicStatistics(StatisticCollection):
    def for_america(self):
        return True

    def for_international(self):
        return True


class InternationalStatistics(StatisticCollection):
    def for_america(self):
        return False

    def for_international(self):
        return True


class USAStatistics(StatisticCollection):
    def for_america(self):
        return True

    def for_international(self):
        return False


class ACSStatisticsColection(StatisticCollection):
    def year(self):
        return 2020

    @abstractmethod
    def acs_name(self):
        pass

    @abstractmethod
    def acs_entity(self):
        pass

    def acs_entity_dict(self):
        return {self.acs_name(): self.acs_entity()}

    def for_america(self):
        return True

    def for_international(self):
        return False

    def compute_statistics(self, shapefile, statistics_table, shapefile_table):
        for entity in self.acs_entity_dict().values():
            acs_data = aggregated_acs_data(self.year(), entity, shapefile)
            for column in acs_data.columns:
                statistics_table[column] = acs_data[column]
        self.mutate_acs_results(statistics_table)

    @abstractmethod
    def mutate_acs_results(self, statistics_table):
        pass


class ACSUSPRStatisticsColection(StatisticCollection):
    def year(self):
        return 2020

    @abstractmethod
    def acs_name(self):
        pass

    @abstractmethod
    def acs_entities(self):
        pass

    def acs_entity_dict(self):
        return {self.acs_name(): self.acs_entities()}

    def for_america(self):
        return True

    def for_international(self):
        return False

    def compute_statistics(self, shapefile, statistics_table, shapefile_table):
        for entities in self.acs_entity_dict().values():
            entity_us, entity_pr = entities
            acs_data = aggregated_acs_data_us_pr(
                self.year(), entity_us, entity_pr, shapefile
            )
            for column in acs_data.columns:
                statistics_table[column] = acs_data[column]
        self.mutate_acs_results(statistics_table)

    @abstractmethod
    def mutate_acs_results(self, statistics_table):
        pass
