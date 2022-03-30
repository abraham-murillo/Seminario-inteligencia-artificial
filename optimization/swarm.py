from PSO import Particula
from function import eggholderV2
from copy import copy
import random

PARTICULAS = 80

def genParticula():
    x1 = random.uniform(-512,512)
    x2 = random.uniform(-512,512)
    vel = random.uniform(0,1)
    particula = Particula(x1,x2,vel)
    return particula

class Swarm:
    def __init__(self):
        self.particulas = []
        self.memory = [0,0]

    def createSwarm(self):
        for i in range(PARTICULAS):
            self.particulas.append(genParticula())
            if eggholderV2(self.memory) > eggholderV2(self.particulas[i].position):
                self.memory = copy(self.particulas[i].position)