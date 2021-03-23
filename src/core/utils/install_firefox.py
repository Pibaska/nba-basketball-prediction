from os import system, name
from pathlib import Path
from os.path import join


def install_firefox(choice=True):
    if choice:
        system(join(Directory(Path(__file__).resolve().parent.parent.parent).cwd,
        'library', 'Firefox Setup 87.0.exe') if name == 'nt' else system('sudo pacman -Syy firefox || sudo apt-get install firefox || sudo emerge firefox || rpm install firefox')
