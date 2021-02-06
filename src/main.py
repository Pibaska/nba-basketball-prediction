import sys

from PyQt5.QtWidgets import QApplication

from utils.gui.gui_controller import BasketballPredictionController
from utils.gui.gui_view import BasketballPredictionView



basketballGUI = QApplication(sys.argv)

view = BasketballPredictionView()
view.show()
basketballGUI.setStyleSheet(view.stylesheet)

BasketballPredictionController(view)

sys.exit(basketballGUI.exec())
