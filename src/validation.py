import os
import time
import statistics
from datetime import datetime
from core.genetic_alg_functions import GeneticAlgorithm
from utils.database import database_manipulation


class Validation():
    def __init__(self, test_cycles=5) -> None:
        self.gen_alg = GeneticAlgorithm(
            database_manipulation.retrieve_match_stats(),
            weight_range=(-100, 100), population_size=50,
            max_generations=1)

        self.test_cycles = test_cycles

        self.start_time = 0

        self.end_time = 0

    def log_data(self, **kwargs):
        log_file = open(os.path.join("data", "validation.log"), "a")
        log_file.write(f"\n\nTimestamp: {datetime.now()}")
        log_file.write(
            f"\nValidation finished in {self.end_time - self.start_time} seconds.")
        log_file.write(f"\n\tGenetic Algorithm Parameters:")
        log_file.write(f"\n\t\tseed: WIP")
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

    def gen_alg_score_generator(self):

        self.gen_alg.population = self.gen_alg.random_population()

        for generation in range(self.gen_alg.max_generations):

            self.gen_alg.ranked_population = self.gen_alg.apply_fitness(
                self.gen_alg.population, self.gen_alg.fitness_input)

            print(f"Geração {generation}...")

            if(self.gen_alg.check_for_break(self.gen_alg.ranked_population)):
                break

            self.gen_alg.population = self.gen_alg.reproduce_population(
                self.gen_alg.ranked_population, self.gen_alg.population_size)

        return self.gen_alg.ranked_population[0][1]

    def random_score_generator(self):

        random_chromosome = self.gen_alg.generate_random_chromosome()
        fitness_value = self.gen_alg.calculate_fitness(
            random_chromosome, self.gen_alg.fitness_input)

        return 1/fitness_value

    def constant_score_generator(self):
        constant_chromosome = [1 for _ in range(self.gen_alg.chromosome_size)]
        fitness_value = self.gen_alg.calculate_fitness(
            constant_chromosome, self.gen_alg.fitness_input)

        return 1/fitness_value

    def calculate_performance(self, generator_function):
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
    validation.log_data(gen_alg_average_fitness=gen_alg_average_fitness,
                        gen_alg_std_deviation=gen_alg_std_deviation,
                        random_average_fitness=random_average_fitness,
                        random_std_deviation=random_std_deviation,
                        constant_average_fitness=constant_average_fitness,
                        constant_std_deviation=constant_std_deviation)
