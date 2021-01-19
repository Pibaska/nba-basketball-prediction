import por_partidas as funcoes

dicionario = {}
diasNosMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


driver = funcoes.SetupDriver(False)

for ano in range(20):
    # calcula se é ano bissexto
    trueAno = 2000 + ano
    bissexto = 1 if (trueAno % 4 == 0 and (trueAno %
                                           400 == 0 or trueAno % 100 != 0)) else 0  # opeador ternário

    for mes in range(12):
        rangeDias = diasNosMeses[mes]

        rangeDias += bissexto if (rangeDias == 28) else 0

        for dia in range(rangeDias):
            funcoes.PuxaJogosDoDia(driver, dia, mes, trueAno)


driver.quit()