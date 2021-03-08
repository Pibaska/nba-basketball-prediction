from random import random
from core.genetic_alg_functions import GeneticAlgorithm
from utils.database import database_manipulation

gen_alg = GeneticAlgorithm(
    database_manipulation.retrieve_match_stats(), weight_magnitude=(-100, 100), population_size=25, max_generations=10)

gen_alg.population = gen_alg.random_population()

for generation in range(gen_alg.max_generations):

    gen_alg.ranked_population = gen_alg.apply_fitness(
        gen_alg.population, gen_alg.fitness_input)

    print(
        f"Geração {generation} | População: '{gen_alg.population[0]} | Fitness: {gen_alg.ranked_population[0][1]}'")

    if(gen_alg.check_for_break(gen_alg.ranked_population)):
        break

    gen_alg.population = gen_alg.reproduce_population(
        gen_alg.ranked_population, gen_alg.population_size)

gen_alg_chromosome = gen_alg.get_results(gen_alg.ranked_population)

random_chromosome = gen_alg.generate_random_chromosome()
fitness_value = gen_alg.calculate_fitness(
    random_chromosome, gen_alg.fitness_input)
scored_individual = (random_chromosome, 1.0/fitness_value)

print(f"AG: {gen_alg_chromosome}", end="\n")
print(f"Random: {scored_individual}", end="\n")
