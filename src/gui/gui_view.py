
import sys
from pathlib import Path
from os.path import join

import gui.gui_fake_data as fake_data
import gui.gui_controller as controller

from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QLineEdit, QMainWindow, QFrame
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore


class BasketballPredictionView(QMainWindow):
    """
    Protótipo da interface gráfica para o programa
    """

    def __init__(self):
        super().__init__()

        with open(join(Path(__file__).resolve().parent, "basketballview.css"), "r") as reader:
            self.stylesheet = reader.read()

        self.setStyleSheet(self.stylesheet)

        self.setWindowTitle('Basketball Prediction - Protótipo')
        self.setMinimumSize(600, 300)

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self._setup_layout())

    def _setup_layout(self):
        """ Faz as configurações necessárias do layout manager"""
        core_layout = QVBoxLayout()
        core_layout.addWidget(self._setup_title_label())
        #core_layout.addWidget(self._setup_scraping_sublayout())
        core_layout.addWidget(self._setup_genalg_sublayout())
        core_layout.addWidget(self._setup_combobox_sublayout())

        return core_layout

    def _setup_title_label(self):
        """Configura a label que diz BASKETBALL PREDICTION bem grande"""
        title_label = QLabel("BASKETBALL PREDICTION")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setObjectName("titleLabel")

        return title_label

    def _setup_scraping_sublayout(self):
        """
        Configura a caixinha que vai ter as comboboxes com os times e a label de PREVER DISPUTA
        """
        layout_widget = QFrame()
        layout_widget.setObjectName("sublayout")

        layout = QGridLayout()

        #self.text_web_scraping = QLabel("1. Colete os dados...")
        self.button_web_scraping = QPushButton("Coletar os dados")
        self.button_web_scraping.setObjectName("bottomButtons")

        #layout.addWidget(self.text_web_scraping, 0, 0,
        #                 alignment=QtCore.Qt.AlignTop)
        layout.addWidget(self.button_web_scraping, 1, 0,
                         alignment=QtCore.Qt.AlignTop)

        layout_widget.setLayout(layout)


        return layout_widget

    def _setup_genalg_sublayout(self):
        layout_widget = QFrame()
        layout_widget.setObjectName("sublayout")

        layout = QGridLayout()

        self.text_gen_alg = QLabel("Preparação...")

        self.button_gen_alg = QPushButton("Gerar lista de fatores")
        self.button_gen_alg.setObjectName("bottomButtons")

        self.button_web_scraping = QPushButton("Coletar os dados")
        self.button_web_scraping.setObjectName("bottomButtons")

        #layout.addWidget(self.text_web_scraping, 0, 0,
        #                 alignment=QtCore.Qt.AlignTop)
        layout.addWidget(self.button_web_scraping, 1, 0,
                         alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(self.text_gen_alg, 0, 0, 
                          alignment=QtCore.Qt.AlignTop)
        layout.addWidget(self.button_gen_alg, 1, 0,
                         alignment=QtCore.Qt.AlignRight)

        layout_widget.setLayout(layout)

        return layout_widget

    def _setup_combobox_sublayout(self):
        """
        Configura a caixinha que vai ter as comboboxes com os times e a label de PREVER DISPUTA
        """
        layout_widget = QFrame()
        layout_widget.setObjectName("predict-sublayout")

        layout = QGridLayout()

        label_predict = QLabel("Prever partida!")

        self.combobox_home = QComboBox()
        for team in fake_data.fake_teams:
            self.combobox_home.addItem(team)
        self.selected_home_team = fake_data.fake_teams[0]

        label_vs = QLabel("VS.")
        label_vs.setAlignment(QtCore.Qt.AlignCenter)
        label_vs.setObjectName("labelVs")

        self.combobox_away = QComboBox()
        for team in fake_data.fake_teams:
            self.combobox_away.addItem(team)
        self.selected_away_team = fake_data.fake_teams[0]

        layout.addWidget(label_predict, 0, 0)

        layout.addWidget(self.combobox_home, 1, 0)
        layout.addWidget(label_vs, 1, 1)
        layout.addWidget(self.combobox_away, 1, 2)

        layout.addWidget(self._setup_prediction_button(), 2, 0, 3, 3)
        layout.addWidget(self._setup_results_text(), 6, 0, 3, 3)

        layout_widget.setLayout(layout)

        return layout_widget

    def _setup_prediction_button(self):
        """Configura o botão de 'Prever!'"""
        self.button_predict = QPushButton("Prever!")
        self.button_predict.setObjectName("predictButton")

        return self.button_predict

    def _setup_results_text(self):
        """Configura o campo no qual vai aparecer o resultado da previsão"""

        self.lineedit_results = QLineEdit("Resultados:")
        self.lineedit_results.setReadOnly(True)
        self.lineedit_results.setAlignment(QtCore.Qt.AlignTop)
        return self.lineedit_results

    def get_comboboxes_teams_content(self):
        return ["Time da Caixa 1", "Time da Caixa 2"]


if __name__ == "__main__":
    basketballGUI = QApplication(sys.argv)

    view = BasketballPredictionView()
    view.show()

    controller.BasketballPredictionController(view)
    basketballGUI.setStyleSheet(view.stylesheet)
    sys.exit(basketballGUI.exec())
