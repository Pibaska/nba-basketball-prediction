import random


class GeneticAlgorithm:
    def __init__(self, model="", good_generations=3):

        self.model = model
        self.chromosome_size = 7  # len(model)
        self.population_size = 100
        self.max_generations = 10000
        self.consecutive_good_generations = 0
        self.target_good_generations = good_generations

        print("Genetic Alg set up!")

    def genetic_alg_loop(self):
        self.population = self.random_population()

        for generation in range(self.max_generations):
            print(f"Geração {generation} | População: '{self.population[0]}'")

            if(self.check_for_break(self.population)):
                break

            ranked_population = self.apply_fitness(self.population)

            self.population = self.reproduce_population(
                ranked_population, self.population_size)

        self.print_results(self.population)

    def random_population(self):
        population = []

        for _ in range(self.population_size):
            chromosome = []

            for _ in range(self.chromosome_size):
                # random.uniform é tipo um randrange mas que retorna floats
                chromosome.append(random.uniform(-10, 10))

            population.append(chromosome)

        return population

    @ staticmethod
    def generate_random_character():
        """Essa função não vai ser necessária quando os times forem passados"""
        return chr(int(random.randrange(32, 255, 1)))

    def check_for_break(self, population: list):
        return self.evaluate_population(population)

    def evaluate_population(self, population):
        """Recebe uma população e diz se ela é boa ou não"""
        # TODO pensar num jeito melhor de avaliar a população

        good_individuals = 0
        for individual in population:
            good_individuals += 1 if individual == self.model else 0

        is_population_good = good_individuals >= int(len(population)/10)

        if(is_population_good):
            self.consecutive_good_generations += 1
        else:
            self.consecutive_good_generations = 0

        return is_population_good

    def apply_fitness(self, population: list):

        ranked_population = []

        for individual in population:
            fitness_value = self.calculate_fitness(individual)

            if fitness_value == 0:
                scored_individual = (individual, 1.0)
            else:
                scored_individual = (individual, 1.0/fitness_value)

            ranked_population.append(scored_individual)

        return ranked_population

    def calculate_fitness(self, chromosome: list):
        fitness = 0
        for i in range(self.chromosome_size):
            fitness += abs(ord(chromosome[i]) - ord(self.model[i]))
        return fitness

    def reproduce_population(self, ranked_population: list, population_size: int):

        reproduced_population = []

        for _ in range(int(population_size)):
            parent1 = self.weighted_choice(ranked_population)
            parent2 = self.weighted_choice(ranked_population)

            child1, child2 = self.crossover(parent1, parent2)

            reproduced_population.append(self.mutation(child1))
            reproduced_population.append(self.mutation(child2))

        return reproduced_population

    @ staticmethod
    def weighted_choice(items):
        total_weight = sum((item[1] for item in items))
        element = random.uniform(0, total_weight)
        for item, weight in items:
            if element < weight:
                return item
            element = element - weight
        return item

    def mutation(self, chromosome):
        chromosome_outside = ""
        mutation_chance = 100
        for i in range(self.chromosome_size):
            if int(random.random() * mutation_chance) == 1:
                chromosome_outside += self.generate_random_character()
            else:
                chromosome_outside += chromosome[i]
        return chromosome_outside

    def crossover(self, chromosome1, chromosome2):
        split_point = int(random.random() * self.chromosome_size)
        return (chromosome1[:split_point] + chromosome2[split_point:],
                chromosome2[:split_point] + chromosome1[split_point:])

    def print_results(self, population: list):
        fit_string = population[0]
        minimum_fitness = self.calculate_fitness(population[0])

        for individual in population:
            fit_individual = self.calculate_fitness(individual)
            print(f"{individual}, {fit_individual}")
            if fit_individual <= minimum_fitness:
                fit_string = individual
                minimum_fitness = fit_individual

        print(f"População Final: {fit_string}")


if __name__ == "__main__":
    gen_alg = GeneticAlgorithm()
    print(gen_alg.random_population())
