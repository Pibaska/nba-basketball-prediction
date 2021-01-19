import por_partidas as funcoes

# prepara o driver
driver = funcoes.SetupDriver(False) 

# cria uma lista de listas de datas ex: [[dia,mes,ano],[dia,mes,ano],[dia,mes,ano],...]]
listaDasDatas = funcoes.TodoDia(driver); 

#para cada dia da lista de datas, busca as informações dos jogos que tiveram
for listaDaData in listaDasDatas:
    funcoes.PuxaJogosDoDia(driver, listaDaData)


driver.quit()