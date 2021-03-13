import sys

from PyQt5.QtWidgets import QApplication
from core import genetic_alg_fake_data

from gui.gui_controller import BasketballPredictionController
from gui.gui_view import BasketballPredictionView
from gui.gui_model import run_gen_alg


# basketballGUI = QApplication(sys.argv)

# view = BasketballPredictionView()
# view.show()
# basketballGUI.setStyleSheet(view.stylesheet)

# BasketballPredictionController(view)

# sys.exit(basketballGUI.exec())

gen_alg = run_gen_alg()
print(gen_alg.predict_match(
    gen_alg.ranked_population[0][0], genetic_alg_fake_data.match_database[0]))

# from web.web_scraping_main import activate_web_scraping
# activate_web_scraping()
