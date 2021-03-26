from os import system, name
import subprocess, sys

if name == 'nt':
    system('python -m venv .')
    system('cmd /c ".\\Scripts\\activate"')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except Exception:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt', '--no-dependencies'])
    finally:
        pass
else:
    system('''
           python -m venv . || python3 -m venv .;
           source ./bin/activate;
           pip install -r requirements.txt || pip install -r config/requirements.txt --no-dependencies;
           clear;''')