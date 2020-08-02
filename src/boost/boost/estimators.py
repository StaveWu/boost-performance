from typing import Union, List
import numpy as np
from . import config


class Estimator:

    def __init__(self, hyper_params: dict, target: int):
        self._require_iterable_value(hyper_params)
        self.hyper_params = hyper_params
        self.target = target

    def tune(self, current_result: Union[int, List[int]]) -> Union[dict, List[dict]]:
        """
        give a better choice when knowing current result
        :param current_result:
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def _require_iterable_value(d: dict):
        for k, v in d.items():
            if not isinstance(v, List):
                raise ValueError(f"invalid pair: {k}-{v}, "
                                 f"expect value as type of iterable but get {type(v)}")


class RandomSearchEstimator(Estimator):

    def __init__(self, hyper_params: dict, target: int):
        super().__init__(hyper_params, target)

    def tune(self, current_result: int) -> dict:
        res = {}
        for k, v in self.hyper_params.items():
            res[k] = np.random.choice(v)
        return res
    

# Generic Algorithm
class Individual:

    genes = None

    def __init__(self, chromosome: dict):
        self.chromosome = chromosome
        self.fitness = None

    @classmethod
    def random_gene(cls, key):
        return np.random.choice(cls.genes[key])

    @classmethod
    def create_gnome(cls):
        chromosome = {}
        for k, v in cls.genes.items():
            chromosome[k] = cls.random_gene(k)
        return cls(chromosome)

    def mate(self, par2):
        """
        mate with par2
        :param par2: Individual
        :return: Individual
        """
        # chromosome for offspring
        child_chromosome = {}
        for key in self.chromosome.keys():

            # random probability
            prob = np.random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome[key] = self.chromosome[key]

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome[key] = par2.chromosome[key]

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome[key] = self.random_gene(key)

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)


class GAEstimator(Estimator):

    def __init__(self, hyper_params: dict, target: int):
        super().__init__(hyper_params, target)
        Individual.genes = hyper_params
        self.population = []
        for _ in range(config.GA["population_size"]):
            self.population.append(Individual.create_gnome())

    def tune(self, current_results: List[int]) -> List[dict]:
        # calc fitness
        for ele, res in zip(self.population, current_results):
            ele.fitness = self.target - res

        # sort the population in increasing order of fitness score
        population = sorted(self.population, key=lambda x: x.fitness)
        if population[0].fitness <= 0:
            raise Exception("we have reached the target")

        new_generation = []
        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * config.GA["population_size"]) / 100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * config.GA["population_size"]) / 100)
        for _ in range(s):
            parent1 = np.random.choice(population[:config.GA["population_size"] // 2])
            parent2 = np.random.choice(population[:config.GA["population_size"] // 2])
            child = parent1.mate(parent2)
            new_generation.append(child)

        self.population = new_generation
        return [ele.chromosome for ele in self.population]









