import random


class AlgoritmoGenetico:
    def __init__(self, model):
        self.model = model
        self.chromosome_size = len(model)
        self.population_size = 100
        self.generations = 10000

    def weighted_choice(self, items):
        total_weight = sum((item[1] for item in items))
        element = random.uniform(0, total_weight)
        for item, weight in items:
            if element < weight:
                return item
            element = element - weight
        return item

    def random_population(self):
        population = []
        for i in range(self.population_size):
            chromosome = ""
            for j in range(self.chromosome_size):
                chromosome += self.random_character()
            population.append(chromosome)
        return population

    def fitness(self, chromosome):
        fitness = 0
        for i in range(self.chromosome_size):
            fitness += abs(ord(chromosome[i]) - ord(self.model[i]))
        return fitness

    def mutation(self, chromosome):
        chromosome_outside = ""
        mutation_chance = 100
        for i in range(self.chromosome_size):
            if int(random.random() * mutation_chance) == 1:
                chromosome_outside += self.random_character()
            else:
                chromosome_outside += chromosome[i]
        return chromosome_outside

    @staticmethod
    def random_character():
        return chr(int(random.randrange(32, 255, 1)))

    def crossover(self, chromosome1, chromosome2):
        position = int(random.random() * self.chromosome_size)
        return (chromosome1[:position] + chromosome2[position:],
                chromosome2[:position] + chromosome1[position:])
