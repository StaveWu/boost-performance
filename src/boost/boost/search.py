from .drivers import TestDriver
from .estimators import Estimator
from .parsers import HyperParamsParser, TestResultParser
from . import config
import json


def search(estimator: Estimator, driver: TestDriver,
           hp_parser: HyperParamsParser, res_parser: TestResultParser) -> None:
    loop = config.NUM_ITERATION
    current_res = -1
    while loop > 0:
        loop -= 1
        hp = estimator.tune(current_res)
        hp_parser.apply_hyper_params(hp)
        driver.run()
        current_res = res_parser.parse_result()
        report(hp, current_res)


def report(hyper_params: dict, test_result: int) -> None:
    with open(config.REPORT_FILE, 'a') as f:
        f.write("\n")
        f.write(f"hyper_params: {json.dumps(hyper_params)}\n")
        f.write(f"result: {test_result}\n")
