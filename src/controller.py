from core.validation.validation import Validation
from core.main import run_gen_alg
from core.validation.validation import Validation
from core.web.control import activate_web_scraping
import time


print("""
    [1] Algoritmo Genético (vai treinar populações com os dados disponiveis no BD)
    [2] Web Scraping (vai coletar dados a partir do dia em que parou, se houver partidas. E salvar no BD)
    [3] Validar projeto
""")

x = input("Queres rodar o que?")

if x == "1":
    print("Rodando AG")
    run_gen_alg()
elif x == "3":
    print("Rodando Validação")
    validation = Validation(test_cycles=1)
    validation.start_time = time.time()

    print("Generating Genetic Algorithm Score")
    gen_alg_stats = validation.calculate_performance(
        validation.gen_alg_score_generator)
    print("Generating Random Score")
    random_stats = validation.calculate_performance(
        validation.random_score_generator)
    print("Generating Constant Score")
    constant_stats = validation.calculate_performance(
        validation.constant_score_generator)

    validation.end_time = time.time()
    validation.dump_json(gen_alg_stats=gen_alg_stats,
                         random_stats=random_stats, constant_stats=constant_stats)

else:
    print("Rodando WS")
    activate_web_scraping()
