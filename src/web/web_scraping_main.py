if __name__ == "__main__":
    import web_scraping_functions as ws_functions
    from utils.database import database_manipulation as db
else:
    import web.web_scraping_functions as ws_functions
    import utils.database.database_manipulation as db


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

        print('---------D-I-A---------')
        print(f'{date[0]}/{date[1]}/{date[2]}')

        match_amount = ws_functions.get_match_amount(driver)
        print(f'Partidas: {match_amount}')

        for item in range(match_amount):
            ws_functions.access_1q_in_box_score(driver, date_url, item)
            team_names, team_tables = ws_functions.get_team_table_names(driver)

            print('--partida--')

            # Aqui em algum lugar vai ter que ter a função de inserir o match
            for i in range(2):
                team_is_home = not i
                team_name = team_names[i].get_text()

                print(f'{team_is_home} - {team_name}')

                team_id = db.create_id()
                lista.append(team_id if team_id else 0)
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
        decimal_indexes = [6, 9, 12]
        integer_indexes = [2, 4, 5, 7, 8, 10, 11,
                           13, 14, 15, 16, 17, 18, 19, 20, 21]

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

        other_team_index = team_part_index+1 if is_team_home else team_part_index - 1

        is_current_team_winner = int(game_data[team_part_index][20]) > int(
            game_data[other_team_index][20])

        game_data[team_part_index].append(int(is_current_team_winner))

        game_data[team_part_index].append(1)  # fk_match INTEGER

        match_list = []    
        if not is_team_home:

            print(game_data)

            db.insert_team_participation_data([game_data[team_part_index -1]])
            db.insert_team_participation_data([game_data[team_part_index]])

            

            match_list.append(date) # fk_team_home INTEGER NOT NULL, criar função para criar os ids
            match_list.append(date) # fk_team_away INTEGER NOT NULL, criar função para criar os ids
            match_list.append(date) # date DATE NOT NULL,  date  

            db.insert_match_data([match_list])

            game_data.clear()
  


if __name__ == "__main__":
    activate_web_scraping()
