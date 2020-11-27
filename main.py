# Packages Import
from Packages.Utils.AGenetico import AlgoritmoGenetico

GeneticUtils = AlgoritmoGenetico(input('Digite um modelo: '))

population = GeneticUtils.random_population()

for generation in range(GeneticUtils.generations):
    print(f"Geração {generation} | População: '{population[0]}'")
    weight_population = []

    if population[0] == GeneticUtils.model:
        break

    for individual in population:
        fitness_value = GeneticUtils.fitness(individual)
        if fitness_value == 0:
            pair = (individual, 1.0)
        else:
            pair = (individual, 1.0 / fitness_value)
        weight_population.append(pair)
    population = []

    for i in range(int(GeneticUtils.population_size)):
        individual1 = GeneticUtils.weighted_choice(weight_population)
        individual2 = GeneticUtils.weighted_choice(weight_population)
        individual1, individual2 = GeneticUtils.crossover(individual1, individual2)
        population.append(GeneticUtils.mutation(individual1))
        population.append(GeneticUtils.mutation(individual2))

fit_string = population[0]
minimum_fitness = GeneticUtils.fitness(population[0])

for individual in population:
    fit_individual = GeneticUtils.fitness(individual)
    if fit_individual <= minimum_fitness:
        fit_string = individual
        minimum_fitness = fit_individual

print(f"População Final: {fit_string}")
