from typing import Union, List

from boost.parsers import HyperParamsParser
from boost.drivers import TestDriver
from boost.estimators import RandomSearchEstimator
from boost.search import search


class GccHyperParamsParser(HyperParamsParser):

    def feed_back(self) -> Union[int, List[int]]:
        pass

    def apply_hyper_params(self, hyper_params: dict) -> None:
        pass


class SpecCPU2017TestDriver(TestDriver):

    def run(self) -> None:
        pass


def get_hyper_params() -> dict:
    return {}


def main():
    parser = GccHyperParamsParser()
    driver = SpecCPU2017TestDriver()
    estimator = RandomSearchEstimator(get_hyper_params(), 1000)
    search(estimator, driver, parser, init_res=-1)


if __name__ == '__main__':
    main()


