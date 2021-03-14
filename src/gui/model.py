# na nossa aplicação de verdade o model seria todos os outros scripts (AG, WS)
# esse arquivo existe pra garantir a flexibilidade da interface
# edit: talvez a gente tenha que manter hein

from datetime import datetime
import time
from genetic_algorithm.functions import GeneticAlgorithm
from utils.database import data_provider
from web_scraping.main import activate_web_scraping
from genetic_algorithm.fake_data import match_database


def predict_score(gen_alg, team_home_name, team_away_name, date, view=None):

    predicted_match = data_provider.get_specific_match_averages(
        team_home_name, team_away_name, date)

    print(predicted_match)

    try:
        match_winner = gen_alg.predict_match(
            gen_alg.ranked_population[0][0], predicted_match)
    except Exception as e:
        print(e)
        raise e

    # view.lineedit_results.setText(
    #     f"Resultados: {view.selected_home_team} ou {view.selected_away_team}")

    print(f"Previsão: {match_winner}")


def activate_home_team_combobox(selected_team, view):
    print(f"combobox home ativada: {selected_team}")
    view.selected_home_team = selected_team


def activate_away_team_combobox(selected_team, view):
    print(f"combobox away ativada: {selected_team}")
    view.selected_away_team = selected_team


def run_gen_alg():
    gen_alg = GeneticAlgorithm(
        data_provider.get_random_match_averages, weight_range=(-100, 100), population_size=50, max_generations=2, fitness_input_size=300, mutation_weight=(-10, 10))

    start_time = time.time()

    gen_alg.population = gen_alg.get_first_generation()

    for generation in range(gen_alg.max_generations):

        gen_alg.ranked_population = gen_alg.apply_fitness(
            gen_alg.population, gen_alg.fitness_input_gatherer)

        print(
            f"Geração {generation} | População: '{gen_alg.population[0]} | Fitness: {gen_alg.ranked_population[0][1]}%'")

        if(gen_alg.ranked_population[0][1] > gen_alg.highest_fitness):
            gen_alg.highest_fitness = gen_alg.ranked_population[0][1]

        if(gen_alg.check_for_break(gen_alg.ranked_population)):
            print("População tá top, hora do break")
            break

        gen_alg.population = gen_alg.reproduce_population(
            gen_alg.ranked_population, gen_alg.population_size)

    end_time = time.time()

    gen_alg.log_and_dump_data(timestamp=datetime.now(),
                              elapsed_time=end_time - start_time)

    return gen_alg


def run_web_scraping():
    activate_web_scraping()
