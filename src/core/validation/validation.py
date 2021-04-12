from json.decoder import JSONDecodeError
from os.path import join
from pathlib import Path
import statistics
import json
from datetime import datetime
import time
from core.gen.classes.genetic_algorithm import GeneticAlgorithm
from data.utils import data_provider


class Validation():
    """Classe usada para fazer a validação dos cromossomos do algoritmo genético
    e salvar esses dados para uso posterior.
    """

    def __init__(self, test_cycles=5, date=[2021, 4, 4]) -> None:
        self.date = date

        self.fitness_input = data_provider.get_matches_averages_by_season(date)

        self.test_cycles = test_cycles

        self.start_time = 0

        self.end_time = 0

    def log_data(self, **kwargs):
        """Função que pega os dados do algoritmo genético e registra
        eles num arquivo validation.log. Na dúvida usar a dump_json() ao
        invés dessa.
        """

        log_file = open(join(Path(__file__).resolve().parent.parent.parent,
                             'data', 'json', 'validation.json'), "a")
        log_file.write(f"\n\nTimestamp: {datetime.now()}")
        log_file.write(
            f"\nValidation finished in {self.end_time - self.start_time} seconds.")

        for score in kwargs:
            log_file.write(f"\n\t{score}: {kwargs[score]}")

        log_file.close()

        print("Data logged!")

    def dump_json(self, **kwargs):
        """Pega os dados do algoritmo genético e acrescenta eles no final
        do arquivo validation.json
        """

        with open(join(Path(__file__).resolve().parent.parent.parent,
                       'data', 'logs', 'genetic_algorithm.log'), "a"):
            validation_data = {
                "general_data": {
                    "timestamp": str(datetime.now()),
                    "validation_duration": self.end_time - self.start_time,
                }
            }

            for score in kwargs:
                validation_data[score] = kwargs[score]

        with open(join(Path(__file__).resolve().parent.parent.parent, "data", "json", "validation.json"), "r") as json_file:
            try:
                data = json.load(json_file)
            except JSONDecodeError:
                data = []

            data.append(validation_data)

        with open(join(Path(__file__).resolve().parent.parent.parent, "data", "json", "validation.json"), "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data dumped into json!")

    def gen_alg_score_generator(self, good_generations=3, weight_range=(-10, 10),
                                mutation_chance=1, mutation_magnitude=(-1, 1), chromosome_size=100,
                                population_size=50, max_generations=100, persistent_individuals=5,
                                random_individuals=5) -> float:
        """Roda o algoritmo genético cujos parâmetros estão especificados
        no __init__

        Returns:
            float: Pontuação de fitness do melhor indivíduo ao final do algoritmo.
        """

        gen_alg = GeneticAlgorithm(
            self.fitness_input, good_generations=good_generations, weight_range=weight_range, mutation_chance=mutation_chance,
            mutation_magnitude=mutation_magnitude, chromosome_size=chromosome_size, population_size=population_size,
            max_generations=max_generations, persistent_individuals=persistent_individuals, timestamp=datetime.now(),
            generate_new_population=True)

        start_time = time.time()

        gen_alg.population = gen_alg.get_first_generation()

        for generation in range(gen_alg.max_generations):
            try:
                gen_alg.current_generation = generation

                gen_alg.ranked_population = gen_alg.apply_fitness(
                    gen_alg.population, gen_alg.fitness_input)

                print(
                    f"Generation {generation} | Best Chromosome: '{gen_alg.population[0]} | Fitness: {gen_alg.ranked_population[0][1]}%'")

                if(gen_alg.ranked_population[0][1] > gen_alg.highest_fitness):
                    gen_alg.highest_fitness = gen_alg.ranked_population[0][1]
                    print(f"New highest fitness: {gen_alg.highest_fitness}")

                if(gen_alg.check_for_break(gen_alg.ranked_population)):
                    print("Population is good; Finish algorithm")
                    break

                gen_alg.population = gen_alg.reproduce_population(
                    gen_alg.ranked_population, gen_alg.population_size)

                if(gen_alg.current_generation % 5 == 0):
                    gen_alg.add_gen_info_to_json()
            except KeyboardInterrupt:
                break

        end_time = time.time()

        gen_alg.log_and_dump_data(timestamp=datetime.now(),
                                  elapsed_time=end_time - start_time)

        return gen_alg.ranked_population[0][1]

    def random_score_generator(self) -> float:
        """Cria um cromossomo com valores aleatórios, dentro do range
        guardado pelo algoritmo genético, especificado no __init__

        Returns:
            float: Pontuação de fitness do cromossomo aleatório
        """
        gen_alg = GeneticAlgorithm(self.fitness_input)

        random_chromosome = gen_alg.generate_random_chromosome()
        fitness_value = gen_alg.calculate_fitness(
            random_chromosome, gen_alg.fitness_input)

        return fitness_value

    def constant_score_generator(self, chromosome) -> float:
        """Gera um cromossomo contendo apenas quantos 1 forem necessários para
        preenchê-lo e retorna seu fitness

        Returns:
            float: O fitness calculado desse cromossomo de valor constante
        """
        gen_alg = GeneticAlgorithm(self.fitness_input)

        fitness_value = gen_alg.calculate_fitness(
            chromosome, gen_alg.fitness_input)

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
