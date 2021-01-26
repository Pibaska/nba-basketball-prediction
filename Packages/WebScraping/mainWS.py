import Packages.WebScraping.por_partidas as funcoes


def activate_web_scraping():
    # prepara o driver
    driver = funcoes.SetupDriver(False)

    # cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
    listaDasDatas = funcoes.TodoDia(driver)

    # para cada dia da lista de datas, busca as informações dos jogos que tiveram
    for listaDaData in listaDasDatas:
        url = funcoes.PuxaJogosDoDia(driver, listaDaData)

        driver.get(url)
        print('---------D-I-A---------')
        print(f'{listaDaData[0]}/{listaDaData[1]}/{listaDaData[2]}')

        qtdJogos = funcoes.ContadorDePartidas(driver)
        print(f'Partidas: {qtdJogos}')

        for i in range(qtdJogos):
            funcoes.EntraNoBoxScore(driver, url, i)
            nomes, tabelasDosTimes = funcoes.FazColeta(driver)

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
                    funcoes.PegaComponente(
                        tabelasDosTimes[x],  itensParaColetar[i], nomeItensParaColetar[i])  # casa

                print('-')

    driver.quit()
