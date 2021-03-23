from core.validation.run import validacao
from core.main import run_gen_alg
from core.web.control import activate_web_scraping
import time


while True:
    x = int(input("""
    [1] Algoritmo Genético (vai treinar populações com os dados disponiveis no BD)
    [2] Web Scraping (vai coletar dados a partir do dia em que parou, se houver partidas e salvar no Banco de Dados)
    [3] Validar projeto

    > """))
    x = run_gen_alg() if x == 1 else activate_web_scraping() if x == 2 else validacao() if x == 3 else 4 
    if x != 4:
        break
