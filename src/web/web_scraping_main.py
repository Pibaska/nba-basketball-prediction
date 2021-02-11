
if __name__ == "__main__": 
    import web_scraping_functions as ws_functions
else:
    import web.web_scraping_functions as ws_functions


id_items_to_collect = ['mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'fg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
names_items_to_collect = ['minutes_played',	'field_goals',	'field_goal_attempts',	'field_goal_percentage',	'3point_field_goals',	'3point_field_goal_attempts',	'3point_field_goals_percentage',	'free_throws',	'free_throw_attempts',	'free_throw_percentage',	'offensive_rebounds',	'defensive_rebounds',	'total_rebounds',	'assists',	'steals',	'blocks',	'turnover', 'personal_faults',	'points']
lista = []
data_game = []

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

                #print(data_game)
                #print('-')
                formating_data(data_game)

        formating_data(data_game)

            # manda esse data pra formatação e da formatação para o banco
            
            
    driver.quit()


def formating_data(data_game):

    #DATA EX  data_game = [['Orlando Magic', 'casa', '39:56', '7', '20', '.350', '0', '0', '.350', '8', '8', '1.000', '4', '5', '9', '1', '1', '0', '5', '4', '22']]

    #função que passa em todos de todos
    for x in range(len(data_game)):
        #for y in range(len(data_game[x])):
        #    data_game[x][y] += "a"
        data_game[x][0] = data_game[x][0]        # team_name VARCHAR
        data_game[x][1] = data_game[x][1]        # team_lcoation VARCHAR 
        data_game[x][2] = data_game[x][1]        # minutes_played INTEGER #vai ser varchar
        data_game[x][3] = int(data_game[x][3])   # field_goals INTEGER
        data_game[x][4] = int(data_game[x][4])   # field_goals_attempts INTEGER
        data_game[x][5] = float(data_game[x][5])   # field_goals_percentage DECIMAL
        data_game[x][6] = int(data_game[x][6])   # 3point_field_goals INTEGER
        data_game[x][7] = int(data_game[x][7])   # 3point_field_goals_attempts INTEGER
        data_game[x][8] = float(data_game[x][8])   # 3point_field_goals_percentage DECIMAL
        data_game[x][9] = int(data_game[x][9])   # free_throws INTEGER
        data_game[x][11] = int(data_game[x][11]) # free_throws_attempts INTEGER
        data_game[x][10] = float(data_game[x][10]) # free_throws_percentage DECIMAL
        data_game[x][12] = int(data_game[x][12]) # offensive_rebounds INTEGER
        data_game[x][13] = int(data_game[x][13]) # defensive_rebounds INTEGER
        data_game[x][14] = int(data_game[x][14]) # total_rebounds INTEGER
        data_game[x][15] = int(data_game[x][15]) # assists INTEGER
        data_game[x][16] = int(data_game[x][16]) # steals INTEGER
        data_game[x][17] = int(data_game[x][17]) # blocks INTEGER
        data_game[x][18] = int(data_game[x][18]) # turnover INTEGER
        data_game[x][19] = int(data_game[x][19]) # personal_faults INTEGER
        data_game[x][20] = int(data_game[x][12]) # points INTEGER
        data_game[x][21] = " temq ver como faz"  # mat_count_by_team INTEGER
        data_game[x][21] = " temq ver como faz"  # won BIT

    print(data_game)
    """
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    team_name VARCHAR(50),
    minutes_played INTEGER,
    field_goals INTEGER,
    field_goals_attempts INTEGER,
    field_goals_percentage DECIMAL(4,3),
    3point_field_goals INTEGER,
    3point_field_goals_attempts INTEGER,
    3point_field_goals_percentage DECIMAL(4,3),
    free_throws INTEGER,
    free_throws_attempts INTEGER,
    free_throws_percentage DECIMAL(4,3),
    offensive_rebounds INTEGER,
    defensive_rebounds INTEGER,
    total_rebounds INTEGER,
    assists INTEGER,
    steals INTEGER,
    blocks INTEGER,
    turnover INTEGER,
    personal_faults INTEGER,
    points INTEGER,
    mat_count_by_team INTEGER,
    won BIT
    """
    pass


if __name__ == "__main__": 
    activate_web_scraping()
