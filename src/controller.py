from core.main import run_gen_alg
from core.web.control import activate_web_scraping


# print("""
#     [1] Algoritmo Genético (vai treinar populações com os dados disponiveis no BD)
#     [2] Web Scraping (vai coletar dados a partir do dia em que parou, se houver partidas. E salvar no BD)
# """)

# x = input("Queres rodar o que?")

# if x == "1":
#     print("Rodando AG")
#     run_gen_alg()
# else:
#     print("Rodando WS")
#     activate_web_scraping()

from data.utils import data_provider
oi = data_provider.get_matches_by_season("2017", 5)
print(oi)
