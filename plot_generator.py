import json
import matplotlib.pyplot as plt

with open("src/data/json/gen/2021-03-24 18:51:31.039277.json", "r") as json_file:
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
plt.ylabel("Melhor Fitness")
plt.show()
