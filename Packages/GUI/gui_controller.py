from PyQt5.QtWidgets import QComboBox
import gui_model as model


class BasketballPredictionController:
    """Classe controladora do modelo MVC"""

    def __init__(self, view):
        self._view = view

        self._connect_signals()

    def _connect_signals(self):
        """Conecta os sinais da view para seus respectivos slots"""

        self._view.button_predict.clicked.connect(model.predict_score)
        self._view.combobox_team1.activated.connect(
            lambda: model.activate_combobox(self._view.combobox_team1.currentText()))
        self._view.combobox_team2.activated.connect(
            lambda: model.activate_combobox(self._view.combobox_team2.currentText()))
