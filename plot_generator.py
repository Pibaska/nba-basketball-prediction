import json
import matplotlib.pyplot as plt
import numpy as np


def plot_gen_alg():
    with open("src/data/json/gen/genetic_algorithm.json", "r") as json_file:
        data = json.load(json_file)
        means = []
        gens = []
        for i in data:
            print(i)
            means.append(i["best_fitness"])
            gens.append(i["current_generation"])

    plt.plot(gens, means)
    plt.title("Evolução do Melhor Fitness por Geração")
    plt.xlabel("Gerações")
    plt.ylabel("Melhor Fitness (%)")
    plt.show()


def plot_validation():
    with open("src/data/json/validation.json", "r") as json_file:
        data = json.load(json_file)

        labels = ['Média', 'Mediana']
        stats = [i["result"] for i in data[-1]["validation_results"]]
        figure = plt.figure()
        axes = figure.add_axes([0, 0, 1, 1])
        axes.bar(["a"], [3])

        plt.show()


if __name__ == "__main__":
    plot_gen_alg()
