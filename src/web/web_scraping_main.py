import web.web_scraping_functions as ws_functions


def activate_web_scraping():
    # prepara o driver
    driver = ws_functions.setup_firefox_driver(False)

    # cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
    date_list = ws_functions.generate_date_list()

    # para cada dia da lista de datas, busca as informações dos jogos que tiveram
    for date in date_list:
        date_url = ws_functions.generate_day_url( date)

        driver.get(date_url)
        print('---------D-I-A---------')
        print(f'{date[0]}/{date[1]}/{date[2]}')

        match_amount = ws_functions.get_match_amount(driver)
        print(f'Partidas: {match_amount}')

        for item in range(match_amount):
            ws_functions.access_1q_in_box_score(driver, date_url, item)
            team_names, team_tables = ws_functions.get_team_table_names(driver)

            id_items_to_collect = ['mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'fg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
            names_items_to_collect = ['minutes_played',	'field_goals',	'field_goal_attempts',	'field_goal_percentage',	'3point_field_goals',	'3point_field_goal_attempts',	'3point_field_goals_percentage',	'free_throws',	'free_throw_attempts',	'free_throw_percentage',	'offensive_rebounds',	'defensive_rebounds',	'total_rebounds',	'assists',	'steals',	'blocks',	'turnover', 'personal_faults',	'points'	]
            print('--partida--')

            for i in range(2):
                team_location = 'casa' if not i else 'fora'
                team_name = team_names[i].get_text()

                print(f'{team_location} - {team_name}')

                for item in range(len(id_items_to_collect)):
                    ws_functions.get_table_values(
                        team_tables[i],  id_items_to_collect[item], names_items_to_collect[item])  # casa

                print('-')

    driver.quit()
