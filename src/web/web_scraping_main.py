
if __name__ == "__main__":
    import web_scraping_functions as ws_functions
    from utils.database import database_manipulation as db
else:
    import web.web_scraping_functions as ws_functions
    import utils.database.database_manipulation as db


id_items_to_collect = ['mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'fg_pct', 'ft',
                       'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
names_items_to_collect = ['minutes_played',	'field_goals',	'field_goal_attempts',	'field_goal_percentage',	'3point_field_goals',	'3point_field_goal_attempts',	'3point_field_goals_percentage',
                          'free_throws',	'free_throw_attempts',	'free_throw_percentage',	'offensive_rebounds',	'defensive_rebounds',	'total_rebounds',	'assists',	'steals',	'blocks',	'turnover', 'personal_faults',	'points']
lista = []
data_game = []


def activate_web_scraping():
    # prepara o driver
    driver = ws_functions.setup_firefox_driver(False)

    # cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
    date_list = ws_functions.generate_date_list()

    # para cada dia da lista de datas, busca as informações dos jogos que tiveram
    for date in date_list:
        date_url = ws_functions.generate_day_url(date)

        driver.get(date_url)

        print('---------D-I-A---------')
        print(f'{date[0]}/{date[1]}/{date[2]}')

        match_amount = ws_functions.get_match_amount(driver)
        print(f'Partidas: {match_amount}')

        for item in range(match_amount):
            ws_functions.access_1q_in_box_score(driver, date_url, item)
            team_names, team_tables = ws_functions.get_team_table_names(driver)

            print('--partida--')

            for i in range(2):
                team_location = 'casa' if not i else 'fora'
                team_name = team_names[i].get_text()

                print(f'{team_location} - {team_name}')

                lista.append(team_name)
                lista.append(team_location)
                for item in range(len(id_items_to_collect)):
                    collected_value = ws_functions.get_table_values(
                        team_tables[i],  id_items_to_collect[item])  # casa

                    #print(f'{names_items_to_collect[item]}: {collected_value}')

                    # vai adicionando os itens numa lista
                    lista.append(collected_value)

                # add na lista os: team_name e team_location

                # coloca a lista no "data"
                data_game.append(lista.copy())
                lista.clear()

                # print(data_game)
                # print('-')
                formatting_data(data_game)

        formatting_data(data_game)

        # manda esse data pra formatação e da formatação para o banco

    driver.quit()


def formatting_data(game_data):

    # função que passa em todos de todos
    for game_index in range(len(game_data)):
        # valores não precisam passar para VARCHAR porque já vêm como string
        decimal_indexes = [5, 8, 11]
        integer_indexes = [1, 3, 4, 6, 7, 9, 10,
                           12, 13, 14, 15, 16, 17, 18, 19, 20]

        for i in decimal_indexes:
            game_data[game_index][i] = float(game_data[game_index][i])
        for i in integer_indexes:
            game_data[game_index][i] = int(float(game_data[game_index][i]))

        game_data[game_index].append(42)  # mat_count_by_team INTEGER
        game_data[game_index].append(1)  # won BIT
        game_data[game_index].append(1)  # fk_match INTEGER

    print(game_data)

    db_connection, cursor = db.open_db()

    db.insert_team_participation_data(cursor, game_data)

    game_data.clear()

    db_connection.commit()

    db.close_db(db_connection)


if __name__ == "__main__":
    activate_web_scraping()
