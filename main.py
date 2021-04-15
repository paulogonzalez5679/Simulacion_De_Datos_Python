import matplotlib.pyplot as plt
import numpy as np
import random
lanzamiento= [int( input("Ingrese numero de lanzamientos:") )]
for i in lanzamiento:
    list = [random.randint(1,6) + random.randint(1,6) for i in range(i)]
    fig, axs = plt.subplots()
    axs.grid(True)
    axs.set_xticks(range(1,20))
    axs.set_title( str(i) + " lanzamientos")
    axs.set_xlabel("Sumatoria")
    axs.set_ylabel("Ocurrencias")
    axs.hist(list, bins=np.arange(1,20)-0.5, rwidth=1, facecolor='black')
    fig.savefig(str(i) + '-dados.png')