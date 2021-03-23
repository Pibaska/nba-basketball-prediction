from os import system


def install_firefox(choice=True):
    if choice:
        system('sudo pacman -Syy firefox || sudo apt-get install firefox || sudo emerge firefox || rpm install firefox')