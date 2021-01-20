# na nossa aplicação de verdade o model seria todos os outros scripts (AG, WS)
# esse arquivo existe pra garantir a flexibilidade da interface

ERROR_MSG = "Error!"


def predict_score(view):
    print("Partida prevista!")
    print(view.selected_home_team, view.selected_away_team)


def activate_home_team_combobox(selected_team, view):
    print(f"combobox home ativada: {selected_team}")
    view.selected_home_team = selected_team


def activate_away_team_combobox(selected_team, view):
    print(f"combobox away ativada: {selected_team}")
    view.selected_away_team = selected_team


def activate_combobox(combobox_text):
    # TODO: transformar essa função numa coisa melhor que preste
    print(f"combobox ativada: {combobox_text}")
