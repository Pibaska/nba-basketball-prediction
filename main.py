from Packages.AlgoritmoGenetico.Base import AlgoritmoGenetico

a = AlgoritmoGenetico(input('Digite um modelo: '))

population = a.random_population()
for generation in range(a.generations):
    print("Geração %s | População: '%s'" % (generation, population[0]))
    weight_population = []
    if population[0] == a.model:
        break
    for individual in population:
        fitness_value = a.fitness(individual)
        if fitness_value == 0:
            pair = (individual, 1.0)
        else:
            pair = (individual, 1.0 / fitness_value)
        weight_population.append(pair)
    population = []
    for i in range(int(a.population_size)):
        individual1 = a.weighted_choice(weight_population)
        individual2 = a.weighted_choice(weight_population)
        individual1, individual2 = a.crossover(individual1, individual2)
        population.append(a.mutation(individual1))
        population.append(a.mutation(individual2))
fit_string = population[0]
minimum_fitness = a.fitness(population[0])
for individual in population:
    fit_individual = a.fitness(individual)
    if fit_individual <= minimum_fitness:
        fit_string = individual
        minimum_fitness = fit_individual
print("População Final: %s" % fit_string)
