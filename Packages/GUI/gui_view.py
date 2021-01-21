import sys
import os

# Esse import vai ter que ser mudado quando esse script for ligado no main
import Packages.GUI.gui_fake_data as fake_data
import Packages.GUI.gui_controller as controller

from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QLineEdit, QMainWindow, QFrame
from PyQt5.QtWidgets import QPushButton
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

        with open(os.path.join(__file__, "..", "basketballview.css"), "r") as reader:
            self.stylesheet = reader.read()

        self.setWindowTitle('Basketball Prediction - Protótipo')
        self.setMinimumSize(600, 400)

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self._setup_layout())

    def _setup_layout(self):
        """ Faz as configurações necessárias do layout manager"""
        core_layout = QVBoxLayout()
        core_layout.addWidget(self._setup_title_label())
        core_layout.addWidget(self._setup_combobox_sublayout())
        core_layout.addWidget(self._setup_prediction_button())
        core_layout.addWidget(self._setup_results_text())
        core_layout.addWidget(self._setup_temporary_buttons())

        return core_layout

    def _setup_title_label(self):
        """Configura a label que diz BASKETBALL PREDICTION bem grande"""
        title_label = QLabel("BASKETBALL PREDICTION")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setObjectName("titleLabel")

        return title_label

    def _setup_combobox_sublayout(self):
        """
        Configura a caixinha que vai ter as comboboxes com os times e a label de PREVER DISPUTA
        """
        layout_widget = QFrame()
        layout_widget.setObjectName("comboboxSublayout")

        layout = QGridLayout()

        # label_predict_match = QLabel("PREVER DISPUTA")
        # label_predict_match.setAlignment(QtCore.Qt.AlignCenter)

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

        layout.addWidget(self.combobox_home, 1, 0)
        layout.addWidget(label_vs, 1, 1)
        layout.addWidget(self.combobox_away, 1, 2)

        layout_widget.setLayout(layout)

        return layout_widget

    def _setup_prediction_button(self):
        """Configura o botão de 'Prever!'"""
        self.button_predict = QPushButton("Prever!")

        return self.button_predict

    def _setup_results_text(self):
        """Configura o campo no qual vai aparecer o resultado da previsão"""

        self.lineedit_results = QLineEdit("Resultados:")
        self.lineedit_results.setReadOnly(True)
        self.lineedit_results.setAlignment(QtCore.Qt.AlignTop)
        return self.lineedit_results

    def _setup_temporary_buttons(self):
        frame_buttons = QFrame(self)
        frame_layout = QGridLayout()

        self.button_gen_alg = QPushButton("Algoritmo Genético")

        self.button_web_scraping = QPushButton("Web Scraping")

        frame_layout.addWidget(self.button_gen_alg, 0, 0)
        frame_layout.addWidget(self.button_web_scraping, 0, 1)

        frame_buttons.setLayout(frame_layout)

        return frame_buttons

    def get_comboboxes_teams_content(self):
        return ["Time da Caixa 1", "Time da Caixa 2"]


def main():
    basketballGUI = QApplication(sys.argv)

    view = BasketballPredictionView()
    view.show()

    controller.BasketballPredictionController(view)
    basketballGUI.setStyleSheet(view.stylesheet)
    sys.exit(basketballGUI.exec())


if __name__ == "__main__":
    main()
