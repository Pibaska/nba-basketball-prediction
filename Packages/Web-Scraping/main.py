import por_partidas as funcoes

# prepara o driver
driver = funcoes.SetupDriver(False) 

# cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
listaDasDatas = funcoes.TodoDia(driver); 

#para cada dia da lista de datas, busca as informações dos jogos que tiveram
for listaDaData in listaDasDatas:
    url = funcoes.PuxaJogosDoDia(driver, listaDaData)

    driver.get(url)
    print('---------D-I-A---------')
    print(f'{listaDaData[0]}/{listaDaData[1]}/{listaDaData[2]}')

    qtdJogos = funcoes.ContadorDePartidas(driver)
    print(f'Partidas: {qtdJogos}')

    for i in range(qtdJogos): 
        funcoes.EntraNoBoxScore(driver, url, i) 
        funcoes.FazColeta(driver)


driver.quit()