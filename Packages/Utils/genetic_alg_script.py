"""
Esse arquivo não vai mais ser útil porque a funcionalidade dele foi refatorada
para a classe GeneticAlgorithm dentro da genetic_alg_functions.py
"""

from Packages.Utils.genetic_alg_functions import GeneticAlgorithm

GeneticUtils = GeneticAlgorithm(input('Digite um modelo: '), 3)

# cria população
population = GeneticUtils.random_population()

# loop principal
for generation in range(GeneticUtils.max_generations):
    # print (não necessário)
    print(f"Geração {generation} | População: '{population[0]}'")
    ranked_population = []

    # checa pra ver se continua
    if GeneticUtils.evaluate_population(population):
        break

    # aplica fitness
    for individual in population:
        fitness_value = GeneticUtils.fitness(individual)
        if fitness_value == 0:
            pair = (individual, 1.0)
        else:
            pair = (individual, 1.0 / fitness_value)
        ranked_population.append(pair)
    population = []

    # reprodução
    for i in range(int(GeneticUtils.population_size)):
        individual1 = GeneticUtils.weighted_choice(ranked_population)
        individual2 = GeneticUtils.weighted_choice(ranked_population)
        individual1, individual2 = GeneticUtils.crossover(
            individual1, individual2)
        population.append(GeneticUtils.mutation(individual1))
        population.append(GeneticUtils.mutation(individual2))

# setup pra dar o print no final
fit_string = population[0]
minimum_fitness = GeneticUtils.fitness(population[0])

for individual in population:
    fit_individual = GeneticUtils.fitness(individual)
    print(f"{individual}, {fit_individual}")
    if fit_individual <= minimum_fitness:
        fit_string = individual
        minimum_fitness = fit_individual

print(f"População Final: {fit_string}")
