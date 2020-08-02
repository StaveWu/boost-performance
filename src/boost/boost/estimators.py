from typing import Iterable
import numpy as np


class Estimator:

    def __init__(self, hyper_params: dict):
        self._require_iterable_value(hyper_params)
        self.hyper_params = hyper_params

    def tune(self, current_result: int) -> dict:
        """
        give a better choice when knowing current result
        :param current_result:
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def _require_iterable_value(d: dict):
        for k, v in d.items():
            if not isinstance(v, Iterable):
                raise ValueError(f"invalid pair: {k}-{v}, "
                                 f"expect value as type of iterable but get {type(v)}")


class RandomSearchEstimator(Estimator):

    def __init__(self, hyper_params: dict):
        super().__init__(hyper_params)

    def tune(self, current_result: int) -> dict:
        res = {}
        for k, v in self.hyper_params.items():
            res[k] = np.random.choice(v)
        return res

