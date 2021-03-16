import sys

# from PyQt5.QtWidgets import QApplication
from genetic_algorithm import fake_data

from gui.controller import BasketballPredictionController
from gui.view import BasketballPredictionView
from gui.model import run_gen_alg
from web_scraping.main import activate_web_scraping
from datetime import datetime as dt


# basketballGUI = QApplication(sys.argv)

# view = BasketballPredictionView()
# view.show()
# basketballGUI.setStyleSheet(view.stylesheet)

# BasketballPredictionController(view)

# sys.exit(basketballGUI.exec())

print("""
    [1] Algoritmo Genético (vai treinar populações com os dados disponiveis no BD)
    [2] Web Scraping (vai coletar dados a partir do dia em que parou, se houver partidas. E salvar no BD)
""")



x = input("Queres rodar o que?")

if x == "1":
    print("Rodando AG")
    run_gen_alg()
else:
    print("Rodando WS")
    activate_web_scraping()

