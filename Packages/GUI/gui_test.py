import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
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

        return core_layout

    def setup_title_label(self):
        title_label = QLabel("BASKETBALL PREDICTION")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        return title_label


def main():
    basketballGUI = QApplication(sys.argv)

    view = BasketballPredictionView()
    view.show()

    sys.exit(basketballGUI.exec())


if __name__ == "__main__":
    main()


# app = QApplication(sys.argv)
# window = QWidget()


# main_layout = QVBoxLayout()

# main_layout.addWidget(QLabel("BASKETBALL PREDICTION"))
# main_layout.addWidget(QLabel('Layout dos combobox'))
# main_layout.addWidget(QPushButton('Prever'))
# main_layout.addWidget(QLineEdit("Resultado:"))

# window.setLayout(main_layout)
# window.show()
# sys.exit(app.exec_())
