from typing import Union, List


class HyperParamsParser:

    def apply_hyper_params(self, hyper_params: Union[dict, List[dict]]) -> None:
        """
        define how to apply hyper params to real test model
        :param hyper_params:
        :return:
        """
        raise NotImplementedError

    def feed_back(self) -> Union[int, List[int]]:
        """
        get test result(s).
        :return:
        """
        raise NotImplementedError

