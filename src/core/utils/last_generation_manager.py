import pickle
from pathlib import Path
from os.path import join

class Last_Generation:
    def __init__(self):
        try:
            with open(join(Path(__file__).resolve().parent.parent.parent.parent,
                           'data', 'bin', 'last_generation.bin'), "rb") as generation_file:
                self.previous_generation = pickle.load(generation_file)
        except Exception as e:
                raise(e)
                          
    def dump(self, population):
        with open(join(Path(__file__).resolve().parent.parent.parent.parent,
                           'data', 'bin', 'last_generation.bin'), "wb") as generation_file:
            pickle.dump(population, generation_file)
