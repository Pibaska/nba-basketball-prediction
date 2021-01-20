import sys

from PyQt5.QtWidgets import QApplication

from Packages.GUI.gui_controller import BasketballPredictionController
from Packages.GUI.gui_view import BasketballPredictionView
from Packages.Utils.genetic_alg_functions import GeneticAlgorithm

# genetic_algorithm = GeneticAlgorithm(model=input("Digite um modelo"))
# genetic_algorithm.genetic_alg_loop()


basketballGUI = QApplication(sys.argv)

view = BasketballPredictionView()
view.show()

BasketballPredictionController(view)
basketballGUI.setStyleSheet(view.stylesheet)
sys.exit(basketballGUI.exec())
