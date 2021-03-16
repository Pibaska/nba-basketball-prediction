import web_scraping.functions as ws_functions
import utils.database.manipulation as db


id_items_to_collect = ['mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft',
                       'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
names_items_to_collect = ['minutes_played',	'field_goals',	'field_goal_attempts',	'field_goal_percentage',	'3point_field_goals',	'3point_field_goal_attempts',	'3point_field_goals_percentage',
                          'free_throws',	'free_throw_attempts',	'free_throw_percentage',	'offensive_rebounds',	'defensive_rebounds',	'total_rebounds',	'assists',	'steals',	'blocks',	'turnover', 'personal_faults',	'points']
lista = []
game_data = []


def activate_web_scraping():
    # prepara o driver
    driver = ws_functions.setup_firefox_driver(False)

    # cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
    date_list = ws_functions.generate_date_list()

    # para cada dia da lista de datas, busca as informações dos jogos que tiveram
    for date in date_list:
        date_url = ws_functions.generate_day_url(date)

        driver.get(date_url)

        print('---------D-A-Y---------')
        print(f'{date[0]}/{date[1]}/{date[2]}')

        match_amount = ws_functions.get_match_amount(driver)
        print(f'Partidas: {match_amount}')

        if match_amount:
            for item in range(match_amount):
                ws_functions.access_1q_in_box_score(driver, date_url, item)
                team_names, team_tables = ws_functions.get_team_table_names(driver)

                print('--partida--')

                # Aqui em algum lugar vai ter que ter a função de inserir o match
                for i in range(2):
                    team_is_home = not i
                    team_name = team_names[i].get_text()

                    print(f'{team_is_home} - {team_name}')

                    lista.append(0)  # posteriormente se tornará participation_id
                    lista.append(db.retrieve_team_id_from_abv((team_name,))[0])
                    lista.append(team_name)
                    lista.append(team_is_home)
                    for item in range(len(id_items_to_collect)):
                        collected_value = ws_functions.get_table_values(
                            team_tables[i],  id_items_to_collect[item])  # casa

                        lista.append(collected_value)

                    game_data.append(lista.copy())
                    lista.clear()

                format_and_insert_team_data(game_data, date)

    driver.quit()


def format_and_insert_team_data(game_data, date):
    is_team_home = False
    # função que passa em todos de todos
    for team_part_index in range(len(game_data)):
        is_team_home = not is_team_home

        # alguns valores não precisam passar para VARCHAR porque já vêm como string
        decimal_indexes = [7, 10, 13]
        integer_indexes = [0, 1, 3, 5, 8, 9, 11,
                           12, 14, 15, 16, 17, 18, 19, 20, 21, 22]

        if float(game_data[team_part_index][4]) == 0:
            print("""
                0 minutos jogados: --------------------------------------
                    dia """+ str(db.get_datetime(date)) +""" 
                    home_team: """ + str(game_data[team_part_index][0]))

        for i in decimal_indexes:
            try:
                game_data[team_part_index][i] = float(
                    game_data[team_part_index][i])
            except ValueError:
                game_data[team_part_index][i] = 0
                print(
                    f"Convertendo valor de {game_data[team_part_index][i]} para 0.")

        for i in integer_indexes:
            try:
                game_data[team_part_index][i] = int(
                    float(game_data[team_part_index][i]))
            except ValueError:
                game_data[team_part_index][i] = 0
                print(
                    f"Convertendo valor de {game_data[team_part_index][i]} para 0.")

        game_data[team_part_index].append(42)  # mat_count_by_team INTEGER

        

    try:
        is_current_team_winner = int(game_data[1][22]) > int(
            game_data[0][22])
    except ValueError:
        is_current_team_winner = 0
    finally:
        game_data[1].append(int(is_current_team_winner))

    try:
        is_current_team_winner = int(game_data[0][22]) > int(
            game_data[1][22])
    except ValueError:
        is_current_team_winner = 0
    finally:
        game_data[0].append(int(is_current_team_winner))


    match_list = []

    game_data[0][0] = (db.create_id_participation())
    db.insert_participation_data([game_data[0]])
    game_data[1][0] = (db.create_id_participation())
    db.insert_participation_data([game_data[1]])

    print([game_data[0]])
    print([game_data[1]])

    # fk_participation_home INTEGER NOT NULL, criar função para criar os ids
    match_list.append(game_data[0][0])
    # fk_participation_away INTEGER NOT NULL, criar função para criar os ids
    match_list.append(game_data[1][0])
    # date DATE NOT NULL,  date
    match_list.append(db.get_datetime(date))

    db.insert_match_data([match_list])

    game_data.clear()


if __name__ == "__main__":
    pass
