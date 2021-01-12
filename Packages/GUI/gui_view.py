import sys
import os

# Esse import vai ter que ser mudado quando esse script for ligado no main
import gui_fake_data as fake_data
import gui_controller as controller

from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QLineEdit, QMainWindow
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

        return core_layout

    def _setup_title_label(self):
        """Configura a label que diz BASKETBALL PREDICTION bem grande"""
        title_label = QLabel("BASKETBALL PREDICTION")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        return title_label

    def _setup_combobox_sublayout(self):
        """
        Configura a caixinha que vai ter as comboboxes com os times e a label de PREVER DISPUTA
        """
        layout_widget = QWidget()

        layout = QGridLayout()

        label_predict_match = QLabel("PREVER DISPUTA")
        label_predict_match.setAlignment(QtCore.Qt.AlignCenter)

        self.combobox_team1 = QComboBox()
        for team in fake_data.fake_teams:
            self.combobox_team1.addItem(team)

        label_vs = QLabel("VS.")
        label_vs.setAlignment(QtCore.Qt.AlignCenter)

        self.combobox_team2 = QComboBox()
        for team in fake_data.fake_teams:
            self.combobox_team2.addItem(team)

        layout.addWidget(label_predict_match, 0, 1)
        layout.addWidget(self.combobox_team1, 1, 0)
        layout.addWidget(label_vs, 1, 1)
        layout.addWidget(self.combobox_team2, 1, 2)

        layout_widget.setLayout(layout)

        return layout_widget

    def _setup_prediction_button(self):
        """Configura o botão de 'Prever!'"""
        self.button_predict = QPushButton("Prever!")

        return self.button_predict

    def _setup_results_text(self):
        """Configura o campo no qual vai aparecer o resultado da previsão"""

        lineedit_results = QLineEdit("Resultados:")
        lineedit_results.setReadOnly(True)
        return lineedit_results

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
