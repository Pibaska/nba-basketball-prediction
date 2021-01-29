import Packages.WebScraping.web_scraping_functions as ws_functions


def activate_web_scraping():
    # prepara o driver
    driver = ws_functions.setup_firefox_driver(False)

    # cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
    listaDasDatas = ws_functions.generate_date_list()

    # para cada dia da lista de datas, busca as informações dos jogos que tiveram
    for listaDaData in listaDasDatas:
        url = ws_functions.access_matches(driver, listaDaData)

        driver.get(url)
        print('---------D-I-A---------')
        print(f'{listaDaData[0]}/{listaDaData[1]}/{listaDaData[2]}')

        qtdJogos = ws_functions.get_match_amount(driver)
        print(f'Partidas: {qtdJogos}')

        for i in range(qtdJogos):
            ws_functions.access_1q_in_box_score(driver, url, i)
            nomes, tabelasDosTimes = ws_functions.get_team_table_names(driver)

            itensParaColetar = ['pts', 'fg', 'fg3']
            nomeItensParaColetar = ['Pontos',
                                    'De 2  ',
                                    'De 3  ']
            print('--partida--')
            for x in range(2):
                local = 'casa' if not x else 'fora'
                nome = nomes[x].get_text()

                print(f'{local} - {nome}')

                for i in range(len(itensParaColetar)):
                    ws_functions.get_table_values(
                        tabelasDosTimes[x],  itensParaColetar[i], nomeItensParaColetar[i])  # casa

                print('-')

    driver.quit()
