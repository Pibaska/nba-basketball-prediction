"""
Interface Simples de um tutorial que eu vi por aí
link: https://realpython.com/python-pyqt-gui-calculator/

Instruções pra rodar isso aqui:
1. Cria um ambiente virtual digitando "python -m venv venv" no terminal
2. Instala o PyQt5 com "pip install -r requirements.txt"
3. Só

~Bernardo
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())
