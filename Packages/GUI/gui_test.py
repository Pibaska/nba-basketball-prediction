import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow
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

        self.setWindowTitle('Basketball Prediction - Protótipo')

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.setup_layout())

    def setup_layout(self):
        """ Faz as configurações necessárias do layout manager"""
        core_layout = QVBoxLayout()
        core_layout.addWidget(self.setup_title_label())
        core_layout.addWidget(self.setup_combobox_sublayout())
        core_layout.addWidget(self.setup_prediction_button())
        core_layout.addWidget(self.setup_results_text())

        return core_layout

    def setup_title_label(self):
        title_label = QLabel("BASKETBALL PREDICTION")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        return title_label

    def setup_combobox_sublayout(self):
        layout_widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(QLabel("A"))
        layout.addWidget(QLabel("B"))
        layout.addWidget(QLabel("C"))

        layout_widget.setLayout(layout)

        return layout_widget

    def setup_prediction_button(self):
        return QPushButton("Prever!")

    def setup_results_text(self):
        return QLineEdit("Resultados:")


def main():
    basketballGUI = QApplication(sys.argv)

    view = BasketballPredictionView()
    view.show()

    sys.exit(basketballGUI.exec())


if __name__ == "__main__":
    main()
