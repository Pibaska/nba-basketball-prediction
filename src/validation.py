import os
from core.genetic_alg_functions import GeneticAlgorithm
from utils.database import database_manipulation

gen_alg = GeneticAlgorithm(
    database_manipulation.retrieve_match_stats(), weight_magnitude=(-100, 100), population_size=25, max_generations=1)

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

log_file = open(os.path.join("data", "validation.log"), "a")
log_file.write(f"\n\nTimestamp: WIP")
log_file.write(f"\nGenetic Algorithm finished in WIP seconds.")
log_file.write(f"\n\tGenetic Algorithm Parameters:")
log_file.write(f"\n\t\tseed: WIP")
log_file.write(f"\n\t\tgood_generations: {gen_alg.target_good_generations}")
log_file.write(f"\n\t\tweight_magnitude: {gen_alg.weight_magnitude}")
log_file.write(f"\n\t\tmutation_chance: {gen_alg.mutation_chance}")
log_file.write(f"\n\t\tchromosome_size: {gen_alg.chromosome_size}")
log_file.write(f"\n\t\tpopulation_size: {gen_alg.population_size}")
log_file.write(f"\n\t\tmax_generations: {gen_alg.max_generations}")
log_file.write(
    f"\n\t\tconsecutive_good_generations: {gen_alg.consecutive_good_generations}")
log_file.write(
    f"\n\tGenetic Algorithm Output:\n\t\tScore: {gen_alg_chromosome[1]}")
for index, stat in enumerate(gen_alg.fitness_input[0]["home_team_stats"]):
    try:
        log_file.write(f"\n\t\t{stat}: {gen_alg_chromosome[0][index]}")
    except IndexError:
        pass
log_file.write(
    f"\n\tRandom Output:\n\t\tScore: {scored_individual[1]}")
for index, stat in enumerate(gen_alg.fitness_input[0]["home_team_stats"]):
    try:
        log_file.write(f"\n\t\t{stat}: {random_chromosome[index]}")
    except IndexError:
        pass
log_file.close()
