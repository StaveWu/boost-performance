
from boost.parsers import HyperParamsParser, TestResultParser
from boost.drivers import TestDriver
from boost.estimators import RandomSearchEstimator
from boost.search import search


class GccHyperParamsParser(HyperParamsParser):

    def apply_hyper_params(self, hyper_params: dict) -> None:
        pass


class SpecCPU2017TestResultParser(TestResultParser):

    def parse_result(self) -> int:
        pass


class SpecCPU2017TestDriver(TestDriver):

    def run(self) -> None:
        pass


def get_hyper_params() -> dict:
    return {}


def main():
    hp_parser = GccHyperParamsParser()
    res_parser = SpecCPU2017TestResultParser()
    driver = SpecCPU2017TestDriver()
    estimator = RandomSearchEstimator(get_hyper_params())
    search(estimator, driver, hp_parser, res_parser)


if __name__ == '__main__':
    main()


