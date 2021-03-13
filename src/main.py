import sys

from PyQt5.QtWidgets import QApplication
from core import genetic_alg_fake_data

from gui.gui_controller import BasketballPredictionController
from gui.gui_view import BasketballPredictionView
from gui.gui_model import predict_score, run_gen_alg


# basketballGUI = QApplication(sys.argv)

# view = BasketballPredictionView()
# view.show()
# basketballGUI.setStyleSheet(view.stylesheet)

# BasketballPredictionController(view)

# sys.exit(basketballGUI.exec())

gen_alg = run_gen_alg()
predict_score(gen_alg, "Orlando Magic", "Miami Heat", [2000, 1, 2])

# from web.web_scraping_main import activate_web_scraping
# activate_web_scraping()
