class CountingDays:
    def RequestCSV(self):
        # --------------------------------- Importações ---------------------------------------#
        import requests
        import json
        import pandas as pd
        # ------------------------------------- URL -------------------------------------------#
        url = "https://api-basketball.p.rapidapi.com/games"
        # -------------------------------    Variaveis     ------------------------------------#
        game = []
        nome_time_casa = []
        nome_time_fora = []
        Pontos_a_b = []
        data_mostrada = []
        # -------------------------------    Requisição    ------------------------------------#
        def cdays():
            global start_date, choice, final_day, fyear, fmonth, fday, syear, sday, smonth
            from datetime import date
            # Data de início -------------------------------------------
            print('\nQual data você deseja começar a contagem?:\n')
            while True:
                try:
                    sday = int(input('Dia: '))
                    smonth = int(input('Mês: '))
                    syear = int(input('Ano: '))
                    start_date = date(syear, smonth, sday)
                    break
                except ValueError:
                    print('\nVocê digitou uma data inexistente, Tente Novamente\n')
                    continue
            year = int(start_date.year)
            month = int(start_date.month)
            day = int(start_date.day)
            # Data Fim -------------------------------------------------
            voltar = []
            while True:
                print('\nQual data você deseja terminar a contagem?:\n')
                fday = int(input('Dia: '))
                fmonth = int(input('Mês: '))
                fyear = int(input('Ano: '))
                if date(fyear, fmonth, fday) >= date(syear, smonth, sday):
                    final_day = date(fyear, fmonth, fday)
                    break
                else:
                    print('\nVocê digitou uma data menor do que a de início\n')
            # -----------------------Loop------------------------------#
            while True:
                try:
                    voltar += [str(start_date.replace(year=year, month=month, day=day))]
                    if start_date.replace(year=year, month=month, day=day) == final_day.replace(year=fyear,
                                                                                                month=fmonth,
                                                                                                day=fday):
                        return voltar
                except ValueError:
                    if month == 1 or 3 or 5 or 7 or 8 or 10:
                        day = 1
                        month += 1
                    elif month == 4 or 6 or 9 or 11:
                        day = 1
                        month += 1
                    elif month == 2:
                        day = 1
                        month += 1
                else:
                    day += 1
                    if (month >= 12) and (day > 31):
                        day = 1
                        month = 1
                        year += 1

            # ---------------------------------------------------------#
        while True:
            data1 = cdays()
            if len(data1) <= 100:
                data = data1
                print(len(data))
                break
            else:
                print('\n+100 Requisições\n')
        for x in data:
            n = 1
            print(x)
            # -------------------------------    API    --------------------------------------#
            querystring = {"season": "2019-2020",
                           "league": "12",
                           "date": x}
            headers = {
                'x-rapidapi-host': "api-basketball.p.rapidapi.com",
                'x-rapidapi-key': "1e20c38f4emsh6507a1941555f53p11dd8bjsn3486fb029733"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            # -------------------------------   JSON    --------------------------------------#
            i = 0
            while (len(json.loads(response.text)["response"])) > i:
                game.append(i)
                data_mostrada.append(x)
                nome_time_casa.append(json.loads(response.text)["response"][i]["teams"]['home']["name"])
                nome_time_fora.append((json.loads(response.text)["response"][i]["teams"]['away']["name"]))
                p_quarto_time_casa = ((json.loads(response.text)["response"][i]["scores"]['home']["quarter_1"]))
                p_quarto_time_fora = ((json.loads(response.text)["response"][i]["scores"]['away']["quarter_1"]))
                Pontos_a_b.append(p_quarto_time_casa - p_quarto_time_fora)
                i = i + 1
                n = n + 1
        # ------------------------------ Modelagem CSV ----------------------------------------#
        df = pd.DataFrame({'Game': game,
                           'Data': data_mostrada,
                           'Nome_Time_Casa': nome_time_casa,
                           'Nome_Time_Fora': nome_time_fora,
                           'Pontos_a-b': Pontos_a_b})
        print('\nFoi obtido o seguinte resultado:\n',df,'\n')
        nameCSV = str(input('\nDigite o nome do seu CSV: \n'))
        df.to_csv(nameCSV+'.csv', index=False, encoding='utf-8')