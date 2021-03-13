import sys

from PyQt5.QtWidgets import QApplication

from gui.gui_controller import BasketballPredictionController
from gui.gui_view import BasketballPredictionView
from gui.gui_model import run_gen_alg


# basketballGUI = QApplication(sys.argv)

# view = BasketballPredictionView()
# view.show()
# basketballGUI.setStyleSheet(view.stylesheet)

# BasketballPredictionController(view)

# sys.exit(basketballGUI.exec())

#run_gen_alg()

from web.web_scraping_main import activate_web_scraping
activate_web_scraping()
