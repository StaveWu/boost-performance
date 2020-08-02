from .drivers import TestDriver
from .estimators import Estimator
from .parsers import HyperParamsParser
from . import config
import json
from typing import Union, List


def search(estimator: Estimator, driver: TestDriver,
           parser: HyperParamsParser, init_res: Union[int, List[int]]) -> None:
    loop = config.NUM_ITERATION
    current_res = init_res
    while loop > 0:
        loop -= 1
        hp = estimator.tune(current_res)
        parser.apply_hyper_params(hp)
        driver.run()
        current_res = parser.feed_back()
        report(hp, current_res)


def report(hyper_params: Union[dict, List[dict]], test_result: Union[int, List[int]]) -> None:
    with open(config.REPORT_FILE, 'a') as f:
        if isinstance(hyper_params, List):
            f.write("\n")
            for hp, res in zip(hyper_params, test_result):
                report_line(hp, res, f)
            return
        report_line(hyper_params, test_result, f)


def report_line(hp, res, f):
    f.write(f"hyper_params: {json.dumps(hp)}\t{res}\n")
