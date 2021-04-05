from pathlib import Path
from os.path import join

class Directory:
    def __init__(self, current_directory = Path(__file__).resolve().parent.parent.parent):
        self.cwd = current_directory