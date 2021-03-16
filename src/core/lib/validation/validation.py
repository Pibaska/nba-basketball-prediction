from json.decoder import JSONDecodeError
import os
import time
import statistics
import json
from datetime import datetime
from genetic_algorithm.functions import GeneticAlgorithm
from utils.database import data_provider


class Validation():
    """Classe usada para fazer a validação dos cromossomos do algoritmo genético
    e salvar esses dados para uso posterior.
    """

    def __init__(self, test_cycles=50) -> None:
        self.gen_alg = GeneticAlgorithm(
            data_provider.get_random_match_averages,
            weight_range=(-100, 100),
            population_size=100,
            max_generations=100,
            mutation_weight=(-10, 10),
            fitness_input_size=200)

        self.test_cycles = test_cycles

        self.start_time = 0

        self.end_time = 0

    def log_data(self, **kwargs):
        """Função que pega os dados do algoritmo genético e registra
        eles num arquivo validation.log. Na dúvida usar a dump_json() ao
        invés dessa.
        """

        log_file = open(os.path.join("data", "validation.log"), "a")
        log_file.write(f"\n\nTimestamp: {datetime.now()}")
        log_file.write(
            f"\nValidation finished in {self.end_time - self.start_time} seconds.")
        log_file.write(f"\n\tGenetic Algorithm Parameters:")
        log_file.write(
            f"\n\t\tgood_generations: {self.gen_alg.target_good_generations}")
        log_file.write(f"\n\t\tweight_magnitude: {self.gen_alg.weight_range}")
        log_file.write(
            f"\n\t\tmutation_chance: {self.gen_alg.mutation_chance}")
        log_file.write(
            f"\n\t\tchromosome_size: {self.gen_alg.chromosome_size}")
        log_file.write(
            f"\n\t\tpopulation_size: {self.gen_alg.population_size}")
        log_file.write(
            f"\n\t\tmax_generations: {self.gen_alg.max_generations}")
        log_file.write(
            f"\n\t\tconsecutive_good_generations: {self.gen_alg.consecutive_good_generations}")

        for score in kwargs:
            log_file.write(f"\n\t{score}: {kwargs[score]}")

        log_file.close()

        print("Data logged!")

    def dump_json(self, **kwargs):
        """Pega os dados do algoritmo genético e acrescenta eles no final
        do arquivo validation.json
        """

        with open(os.path.join("data", "validation.json")) as json_file:
            validation_data = {
                "general_data": {
                    "timestamp": str(datetime.now()),
                    "validation_duration": self.end_time - self.start_time,
                },
                "genetic_algorithm_data": {
                    "seed": "WIP",
                    "good_generations": self.gen_alg.target_good_generations,
                    "weight_range": self.gen_alg.weight_range,
                    "mutation_chance": self.gen_alg.mutation_chance,
                    "chromosome_size": self.gen_alg.chromosome_size,
                    "population_size": self.gen_alg.population_size,
                    "max_generations": self.gen_alg.max_generations
                }
            }

            for score in kwargs:
                validation_data[score] = kwargs[score]

            try:
                data = json.load(json_file)
            except JSONDecodeError:
                data = []

            data.append(validation_data)

        with open(os.path.join("data", "validation.json"), "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data dumped into json!")

    def gen_alg_score_generator(self) -> float:
        """Roda o algoritmo genético cujos parâmetros estão especificados
        no __init__

        Returns:
            float: Pontuação de fitness do melhor indivíduo ao final do algoritmo.
        """

        # Pensar se isso aqui deve ser mantido aleatório ou pegar das outras coisas também
        self.gen_alg.population = self.gen_alg.random_population()

        for generation in range(self.gen_alg.max_generations):

            self.gen_alg.ranked_population = self.gen_alg.apply_fitness(
                self.gen_alg.population, self.gen_alg.fitness_input_gatherer)

            print(f"Geração {generation}...")

            if(self.gen_alg.check_for_break(self.gen_alg.ranked_population)):
                break

            self.gen_alg.population = self.gen_alg.reproduce_population(
                self.gen_alg.ranked_population, self.gen_alg.population_size)

        return self.gen_alg.ranked_population[0][1]

    def random_score_generator(self) -> float:
        """Cria um cromossomo com valores aleatórios, dentro do range
        guardado pelo algoritmo genético, especificado no __init__

        Returns:
            float: Pontuação de fitness do cromossomo aleatório
        """
        fitness_input = []

        for _ in range(self.gen_alg.fitness_input_size):
            fitness_input.append(self.gen_alg.fitness_input_gatherer())

        random_chromosome = self.gen_alg.generate_random_chromosome()
        fitness_value = self.gen_alg.calculate_fitness(
            random_chromosome, fitness_input)

        return fitness_value

    def constant_score_generator(self) -> float:
        """Gera um cromossomo contendo apenas quantos 1 forem necessários para
        preenchê-lo e retorna seu fitness

        Returns:
            float: O fitness calculado desse cromossomo de valor constante
        """
        fitness_input = []

        for _ in range(self.gen_alg.fitness_input_size):
            fitness_input.append(self.gen_alg.fitness_input_gatherer())

        constant_chromosome = [1 for _ in range(self.gen_alg.chromosome_size)]
        fitness_value = self.gen_alg.calculate_fitness(
            constant_chromosome, fitness_input)

        return fitness_value

    def calculate_performance(self, generator_function) -> dict:
        """Roda uma função geradora de pontuações de fitness várias vezes,
        salva esses resultados em uma lista e retorna um dicionário contendo
        informações sobre as pontuações registradas

        Args:
            generator_function (function): A função que vai retornar os fitness
            que serão adicionados na lista

        Returns:
            dict: Dados sobre a lista de pontuações de fitness, respectivamente:
            média, desvio padrão, mediana e variância.
        """

        result_list = []

        for cycle in range(self.test_cycles):
            result_list.append(generator_function())

            print(f"Cycle {cycle} Finished!")

        result_statistics = {
            "mean": statistics.mean(result_list),
            "std_deviation": statistics.pstdev(result_list),
            "median": statistics.median(result_list),
            "variance": statistics.pvariance(result_list)
        }

        return result_statistics


if __name__ == "__main__":
    validation = Validation()
    validation.start_time = time.time()

    print("Generating Genetic Algorithm Score")
    gen_alg_stats = validation.calculate_performance(
        validation.gen_alg_score_generator)
    print("Generating Random Score")
    random_stats = validation.calculate_performance(
        validation.random_score_generator)
    print("Generating Constant Score")
    constant_stats = validation.calculate_performance(
        validation.constant_score_generator)

    validation.end_time = time.time()
    validation.dump_json(gen_alg_stats=gen_alg_stats,
                         random_stats=random_stats, constant_stats=constant_stats)
