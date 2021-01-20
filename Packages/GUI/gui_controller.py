from PyQt5.QtWidgets import QComboBox
import Packages.GUI.gui_model as model


class BasketballPredictionController:
    """Classe controladora do modelo MVC"""

    def __init__(self, view):
        self._view = view

        self._connect_signals()

    def _connect_signals(self):
        """Conecta os sinais da view para seus respectivos slots"""

        self._view.button_predict.clicked.connect(
            lambda: model.predict_score(self._view))
        self._view.combobox_home.activated.connect(
            lambda: model.activate_home_team_combobox(self._view.combobox_home.currentText(), self._view))
        self._view.combobox_away.activated.connect(
            lambda: model.activate_away_team_combobox(self._view.combobox_away.currentText(), self._view))
