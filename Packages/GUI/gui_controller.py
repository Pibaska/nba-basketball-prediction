class BasketballPredictionController:
    """Classe controladora do modelo MVC"""

    def __init__(self, view):
        self._view = view

        self._connect_signals()

    def _connect_signals(self):
        """Conecta os sinais da view para seus respectivos slots"""

        self._view.button_predict.clicked.connect(lambda: print("Prever!"))
