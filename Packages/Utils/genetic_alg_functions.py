import random
# Esse import precisa mudar se esse código for chamado pelo main
import genetic_alg_fake_data


class GeneticAlgorithm:
    def __init__(self, model: dict, good_generations=3):

        self.model = model
        self.target_good_generations = good_generations

        self.chromosome_size = 7
        self.weight_magnitude = (-10, 10)
        self.population_size = 100
        self.max_generations = 10000
        self.consecutive_good_generations = 0

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
                chromosome.append(random.uniform(
                    self.weight_magnitude[0], self.weight_magnitude[1]))

            population.append(chromosome)

        return population

    def check_for_break(self, population: list):
        """Essa função parece meio inútil mas permite que a gente procure por
        gerações boas consecutivas antes de parar o algoritmo
        """

        return self.evaluate_population(population)

    def evaluate_population(self, population: list):
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
            fitness_value = self.calculate_fitness(individual, self.model)

            if fitness_value == 0:
                scored_individual = (individual, 1.0)
            else:
                scored_individual = (individual, 1.0/fitness_value)

            ranked_population.append(scored_individual)

        return ranked_population

    def calculate_fitness(self, chromosome: list, match_data: dict):
        """Calcula o valor de fitness de um cromossomo.
        Obs.: Por enquanto tá extremamente mal otimizado

        Args:
            chromosome (list): O cromossomo a ser avaliado;
            match_data (dict): Os dados verdadeiros dos jogos para comparar com o cromossomo;

        Returns:
            fitness (int): O fitness do cromossomo. Quanto menor o valor, melhor;
        """

        fitness = 0
        for current_match in match_data:
            home_team_stats = match_data[current_match]["home_team_stats"]
            home_team_parsed_stats = [
                home_team_stats["average_1q_score"] * chromosome[0],
                home_team_stats["1q_home_ratio"] * chromosome[1],
                home_team_stats["1q_home_spread"] * chromosome[2],
                home_team_stats["1q_last10games_ratio"] * chromosome[5],
                home_team_stats["1q_last10games_spread"] * chromosome[6]
            ]
            away_team_stats = match_data[current_match]["away_team_stats"]
            away_team_parsed_stats = [
                away_team_stats["average_1q_score"] * chromosome[0],
                away_team_stats["1q_away_ratio"] * chromosome[3],
                away_team_stats["1q_away_spread"] * chromosome[4],
                away_team_stats["1q_last10games_ratio"] * chromosome[5],
                away_team_stats["1q_last10games_spread"] * chromosome[6]
            ]

            home_team_score = sum(home_team_parsed_stats)
            away_team_score = sum(away_team_parsed_stats)

            real_1q_winner = match_data[current_match]["1q_winner"]
            predicted_1q_winner = "home" if home_team_score > away_team_score else "away" if home_team_score < away_team_score else "tie"

            # 1 se for True, 0 se for False
            fitness += int(real_1q_winner != predicted_1q_winner)

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
                # TODO: substituir isso por algo que funcione
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
        minimum_fitness = self.calculate_fitness(
            population[0], self.model)

        for individual in population:
            fit_individual = self.calculate_fitness(
                individual, self.model)
            print(f"{individual}, {fit_individual}")
            if fit_individual <= minimum_fitness:
                fit_string = individual
                minimum_fitness = fit_individual

        print(f"População Final: {fit_string}")


if __name__ == "__main__":
    gen_alg = GeneticAlgorithm(genetic_alg_fake_data.match_database)
    chromosome = [1, 1, 1, 1, 1, 1, 1]
    print(gen_alg.calculate_fitness(chromosome,
                                    genetic_alg_fake_data.match_database))
