# na nossa aplicação de verdade o model seria todos os outros scripts (AG, WS)
# esse arquivo existe pra garantir a flexibilidade da interface
# edit: talvez a gente tenha que manter hein

from core.genetic_alg_functions import GeneticAlgorithm
from utils.database import database_manipulation
from web.web_scraping_main import activate_web_scraping


def predict_score(view):
    view.lineedit_results.setText(
        f"Resultados: {view.selected_home_team} ou {view.selected_away_team}")


def activate_home_team_combobox(selected_team, view):
    print(f"combobox home ativada: {selected_team}")
    view.selected_home_team = selected_team


def activate_away_team_combobox(selected_team, view):
    print(f"combobox away ativada: {selected_team}")
    view.selected_away_team = selected_team


def run_gen_alg():
    genetic_algorithm = GeneticAlgorithm(
        database_manipulation.retrieve_match_stats())
    genetic_algorithm.genetic_alg_loop()


def run_web_scraping():
    activate_web_scraping()
