
class HyperParamsParser:

    def apply_hyper_params(self, hyper_params: dict) -> None:
        """
        define how to apply hyper params to real test model
        :param hyper_params:
        :return:
        """
        raise NotImplementedError


class TestResultParser:

    def parse_result(self) -> int:
        """
        to get test result
        :return:
        """
        raise NotImplementedError

