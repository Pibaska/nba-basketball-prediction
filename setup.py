from os import system, name


if name == 'nt':
    system('python -m venv .')
    system('./Scripts/activate.bat')
    try:
        system('pip install -r requirements.txt')
    except Exception:
        system('pip install -r requirements.txt --no-dependencies')
    finally:
        pass
else:
    system('''
           python -m venv . || python3 -m venv .;
           source ./bin/activate;
           pip install -r requirements.txt || pip install -r config/requirements.txt --no-dependencies;
           ''')