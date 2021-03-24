
from datetime import datetime
import time
from core.gen.classes.genetic_algorithm import GeneticAlgorithm
from data.utils import data_provider
from core.web.control import activate_web_scraping


def predict_score(team_home_name, team_away_name, date, view=None):
    gen_alg = GeneticAlgorithm([])
    weight_list = gen_alg.get_first_generation()[0]

    predicted_match = data_provider.get_specific_match_averages(
        team_home_name, team_away_name, date)

    print(predicted_match)

    try:
        match_winner = gen_alg.predict_match(
            weight_list, predicted_match)
        match_winner_name = team_home_name if match_winner == "team_home" else team_away_name
        print(f"Winner: {match_winner_name}")
    except Exception as e:
        raise e

    # view.lineedit_results.setText(
    #     f"Resultados: {view.selected_home_team} ou {view.selected_away_team}")


def run_gen_alg(date=[2018, 6, 20],
                good_generations=3,
                weight_range=(-10, 10),
                mutation_chance=1,
                mutation_magnitude=(-1, 1),
                chromosome_size=100,
                population_size=50,
                max_generations=100,
                persistent_individuals=5):

    input_matches = data_provider.get_matches_averages_by_season(date)

    gen_alg = GeneticAlgorithm(
        input_matches, good_generations=good_generations, weight_range=weight_range, mutation_chance=mutation_chance,
        mutation_magnitude=mutation_magnitude, chromosome_size=chromosome_size, population_size=population_size,
        max_generations=max_generations, generation_persistent_individuals=persistent_individuals)

    start_time = time.time()

    gen_alg.population = gen_alg.get_first_generation()

    for generation in range(gen_alg.max_generations):
        try:
            gen_alg.current_generation = generation

            gen_alg.ranked_population = gen_alg.apply_fitness(
                gen_alg.population, gen_alg.fitness_input)

            print(
                f"Geração {generation} | População: '{gen_alg.population[0]} | Fitness: {gen_alg.ranked_population[0][1]}%'")

            if(gen_alg.ranked_population[0][1] > gen_alg.highest_fitness):
                gen_alg.highest_fitness = gen_alg.ranked_population[0][1]
                print(gen_alg.highest_fitness)

            if(gen_alg.check_for_break(gen_alg.ranked_population)):
                print("População tá top, hora do break")
                break

            gen_alg.population = gen_alg.reproduce_population(
                gen_alg.ranked_population, gen_alg.population_size)
        except KeyboardInterrupt:
            break

    end_time = time.time()

    gen_alg.log_and_dump_data(timestamp=datetime.now(),
                              elapsed_time=end_time - start_time)

    return gen_alg


def run_web_scraping():
    activate_web_scraping()

# def activate_home_team_combobox(selected_team, view):
#   print(f"combobox home ativada: {selected_team}")
#   view.selected_home_team = selected_team
#
# def activate_away_team_combobox(selected_team, view):
#   print(f"combobox away ativada: {selected_team}")
#   view.selected_away_team = selected_team
#
