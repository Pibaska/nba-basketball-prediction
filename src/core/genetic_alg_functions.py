import random


class GeneticAlgorithm:
    def __init__(self, fitness_input: dict, good_generations=3,
                 weight_magnitude=(-10, 10), mutation_chance=100,
                 chromosome_size=19, population_size=50,
                 max_generations=100):
        """Fornece as funções necessárias para rodar um algoritmo genético.

        Args:
            fitness_input (dict): Dicionário contendo valores que serão usados dentro da função fitness para avaliar cada indivíduo
            good_generations (int, optional): Número de gerações "boas" consecutivas necessárias para o algoritmo ser interrompido. 
            Defaults to 3.

            weight_magnitude (tuple, optional): Valores mínimos e máximos para um gene nos cromossomos. Defaults to (-10, 10).

            mutation_chance (int, optional): Define a chance de ocorrer uma mutação, que é calculada em cada gene. Defaults to 100.

            chromosome_size (int, optional): Define quantos genes estarão presentes em cada indivíduo/cromossomo. Defaults to 20.

            population_size (int, optional): Tamanho da população para cada geração. Na primeira geração é o valor definido, 
            sendo que nas gerações subsequentes o números de indivíduos será sempre 2x o número especificado aqui. Defaults to 50.

            max_generations (int, optional): Quantidade máxima de gerações para serem criadas antes que o algoritmo seja interrompido. 
            Defaults to 100.
        """

        self.fitness_input = fitness_input

        self.target_good_generations = good_generations

        # Define o quanto os pesos vão influenciar nos atributos
        self.weight_magnitude = weight_magnitude

        self.mutation_chance = mutation_chance

        self.chromosome_size = chromosome_size

        # x na primeira geração, nas outras vira 2x
        self.population_size = population_size

        self.max_generations = max_generations

        self.consecutive_good_generations = 0

        print("Genetic Alg set up!")

    def random_population(self):
        """Preenche uma população com indivíduos gerados aleatoriamente

        Returns:
            (list): População preenchida com os indivíduos lindinhos

        Complexidade: O(p*c)
            p = Tamanho desejado da população
            c = Tamanho de cada cromossomo
        """
        population = []

        for _ in range(self.population_size):
            chromosome = []

            for i in range(self.chromosome_size):
                # random.uniform é tipo um randrange mas que retorna floats
                chromosome.append(random.uniform(
                    self.weight_magnitude[0], self.weight_magnitude[1]))

            population.append(chromosome)

        return population

    def check_for_break(self, population: list):
        """Parece meio inútil porque só chama outra função mas o propósito dela é
        ser extendida caso quisermos fazer com que o algoritmo pare com condições mais elaboradas.

        Args:
            population (list): A população a ser avaliada

        Returns:
            bool: True se o algoritmo genético estiver pronto para ser parado
        """

        return self.evaluate_population(population)

    def evaluate_population(self, population: list):
        """Julga se uma lista de indivíduos é boa ou não segundo os critérios
        definidos dentro dela. Por enquanto o critério é 1/10 da população ter
        uma pontuação de 0, ou seja, 10 conjuntos de pesos acertarem todas as
        partidas (talvez seja meio exigente).

        Args:
            population (list): A lista a ser avaliada;

        Returns:
            bool: True se a população for boa segundo os critérios;

        Complexidade: O(p)
            p = Quantidade de indivíduos na população
        """

        # TODO pensar num jeito melhor de avaliar a população

        good_individuals = 0
        for individual in population:
            good_individuals += individual[1] == 0

        is_population_good = good_individuals >= int(len(population)/10)

        if(is_population_good):
            self.consecutive_good_generations += 1
        else:
            self.consecutive_good_generations = 0

        return is_population_good

    def apply_fitness(self, population: list, fitness_input: list):
        """Aplica uma pontuação para cada indivíduo da população usando uma
         função fitness definida.

        Args:
            population (list): A população a ser avaliada
            fitness_input (list): A lista de dados para o qual os cromossomos
            serão otimizados.

        Returns:
            (list): Uma lista contendo elementos no formato (indivíduo, pontuação)

        Complexidade: O(p)
            p: Quantidade de indivíduos dentro de uma população
        """

        ranked_population = []

        for individual in population:
            fitness_value = self.calculate_fitness(
                individual, fitness_input)

            if fitness_value == 0:
                scored_individual = (individual, 1.0)
            else:
                scored_individual = (individual, 1.0/fitness_value)

            ranked_population.append(scored_individual)

        return ranked_population

    def calculate_fitness(self, chromosome: list, match_data: dict):
        """Calcula o valor de fitness de um cromossomo.
        Obs.: Por enquanto tá extremamente mal otimizado
        Sugestão: Registrar um erro do vetor de pesos apenas se tiver
        uma diferença considerável entre as pontuações dos 2 times

        Args:
            chromosome (list): O cromossomo a ser avaliado;
            match_data (dict): Os dados verdadeiros dos jogos para comparar com o cromossomo;

        Returns:
            fitness (int): O fitness do cromossomo. Quanto menor o valor, melhor;

        Complexidade: O(m):
            m: Quantidade de partidas presentes em match_data
        """

        fitness = 0
        for current_match in match_data:
            home_team_stats = current_match["home_team_stats"]
            home_team_parsed_stats = []

            for gene_index, stats in enumerate(home_team_stats):
                try:
                    home_team_parsed_stats.append(
                        home_team_stats[stats] * chromosome[gene_index])
                except IndexError:
                    pass
                    # print(
                    #     "IndexError acontecendo por causa do valor de 'won'. Conserta isso Berb!")

            away_team_stats = current_match["away_team_stats"]
            away_team_parsed_stats = []

            for gene_index, stats in enumerate(away_team_stats):
                try:
                    away_team_parsed_stats.append(
                        away_team_stats[stats] * chromosome[gene_index])
                except IndexError:
                    pass
                    # print(
                    #     "IndexError acontecendo por causa do valor de 'won'. Conserta isso Berb!")

            home_team_score = sum(home_team_parsed_stats)
            away_team_score = sum(away_team_parsed_stats)

            real_1q_winner = "home" if home_team_stats["won"] else "away"
            predicted_1q_winner = "home" if home_team_score > away_team_score else "away"

            # 1 se for True, 0 se for False
            fitness += int(real_1q_winner != predicted_1q_winner)

        return fitness

    def reproduce_population(self, ranked_population: list, population_size: int):
        """Função responsável por delegar a reprodução de uma geração a outras
        funções mais específicas

        Args:
            ranked_population (list): Uma lista de indivíduos com seus pesos
            population_size (int): O tamanho desejado para a população.

        Returns:
            [list]: Uma lista com novos indivíduos após a reprodução ter acontecido.
        """

        reproduced_population = []

        for _ in range(int(population_size)):
            parent1 = self.weighted_choice(ranked_population)
            parent2 = self.weighted_choice(ranked_population)

            child1, child2 = self.crossover(parent1, parent2)

            reproduced_population.append(self.mutation(child1))
            reproduced_population.append(self.mutation(child2))
        return reproduced_population

    @staticmethod
    def weighted_choice(weighted_items):
        """Escolhe um item dentro de uma lista com os itens e seus pesos,
        dando prioridade para itens com peso maior

        Args:
            weighted_items ([list]): Uma lista contendo itens no formato (item, peso)

        Returns:
            item: O item escolhido a partir do peso
        """

        total_weight = sum((item[1] for item in weighted_items))
        element = random.uniform(0, total_weight)
        for item, weight in weighted_items:
            if element < weight:
                return item
            element = element - weight
        return item

    def crossover(self, parent1: list, parent2: list):
        """Recebe os genes de dois pais, realiza o crossing-over e
        retorna dois filhos

        Args:
            parent1 (list): Um dos indivíduos cujos genes serão repassados
            parent2 (list): O outro indivíduo cujos genes serão repassados

        Returns:
            ([list],[list]): Os dois filhos gerados a partir dos pais
        """

        split_point = int(random.random() * self.chromosome_size)

        return (parent1[:split_point] + parent2[split_point:],
                parent2[:split_point] + parent1[split_point:])

    def mutation(self, chromosome: list):
        """Percorre por todos os genes de um cromossomo recebido, e,
        dada uma chance definida por GeneticAlgorithm.mutation_chance,
        pode substituir os genes originais por novos genes criados aleatoriamente.

        Args:
            chromosome (list): O cromossomo a ser percorrido

        Returns:
            [list]: O cromossomo após ter passado pelo processo de mutação
        """

        mutated_chromosome = []
        for i in range(self.chromosome_size):

            if int(random.random() * self.mutation_chance) == 1:
                mutated_chromosome.append(random.uniform(
                    self.weight_magnitude[0], self.weight_magnitude[1]))
            else:
                mutated_chromosome.append(chromosome[i])

        return mutated_chromosome

    def get_results(self, population: list):
        print("Algoritmo terminado!")

        fit_string = population[0]
        minimum_fitness = self.calculate_fitness(
            population[0], self.fitness_input)

        for individual in population:
            fit_individual = self.calculate_fitness(
                individual, self.fitness_input)
            if fit_individual <= minimum_fitness:
                fit_string = individual
                minimum_fitness = fit_individual

        print(
            f"População Final: {fit_string}, {self.calculate_fitness(fit_string, self.fitness_input)}")

        return fit_string
