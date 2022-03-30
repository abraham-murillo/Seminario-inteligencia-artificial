from function import eggholder
from swarm import Swarm
from function import eggholderV2
from random import uniform
from copy import copy
import matplotlib.pyplot as plt

# Constantes del problema
iteration = 50
W = 1
P1 = 1.5
P2 = 1.4

swarm = Swarm()
swarm.createSwarm()
evaluation = []
average = []
sum = 0

for i in range(iteration):
    for j in range(len(swarm.particulas)):
        swarm.particulas[j].velocityX1 = W * swarm.particulas[j].velocityX1 + P1 * uniform(0, 1) * (
            swarm.particulas[j].localMemory[0] - swarm.particulas[j].position[0]) + P2 * uniform(0, 1) * (swarm.memory[0] - swarm.particulas[j].position[0])
        swarm.particulas[j].velocityX2 = W * swarm.particulas[j].velocityX2 + P1 * uniform(0, 1) * (
            swarm.particulas[j].localMemory[1] - swarm.particulas[j].position[1]) + P2 * uniform(0, 1) * (swarm.memory[1] - swarm.particulas[j].position[1])

        swarm.particulas[j].position[0] = swarm.particulas[j].position[0] + \
            swarm.particulas[j].velocityX1
        if (swarm.particulas[j].position[0] > 512):
            swarm.particulas[j].position[0] = 512
        if (swarm.particulas[j].position[0] < -512):
            swarm.particulas[j].position[0] = -512

        swarm.particulas[j].position[1] = swarm.particulas[j].position[1] + \
            swarm.particulas[j].velocityX2
        if (swarm.particulas[j].position[1] > 512):
            swarm.particulas[j].position[1] = 512
        if (swarm.particulas[j].position[1] < -512):
            swarm.particulas[j].position[1] = -512

        if eggholderV2(swarm.particulas[j].position) < eggholderV2(swarm.particulas[j].localMemory):
            swarm.particulas[j].localMemory = copy(
                swarm.particulas[j].position)

        if eggholderV2(swarm.particulas[j].position) < eggholderV2(swarm.memory):
            swarm.memory = copy(swarm.particulas[j].position)

    print(f'Iteration {i}, Function: ', eggholderV2(
        swarm.memory), '\nParticle: ', swarm.memory)

    evaluation.append(eggholderV2(swarm.memory))

    sum += evaluation[-1]
    average.append(sum / (i + 1))

plt.plot(evaluation, color="blue")
plt.plot(average, color="red")

plt.xlabel("Iterations")
plt.ylabel("Min/ average")
plt.title("Average fitness over iterations")
plt.show()
