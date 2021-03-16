from os import system, name


if name == 'nt':
    system('python -m venv config/env')
    system('config/env/Scripts/activate.bat')
    try:
        system('pip install -r config/requirements.txt')
    except Exception:
        system('pip install -r config/requirements.txt --no-dependencies')
    finally:
        pass
else:
    system('''
           python -m venv config/env || python3 -m venv config/env;
           source config/env/bin/activate;
           pip install -r config/requirements.txt || pip install -r config/requirements.txt --no-dependencies''')