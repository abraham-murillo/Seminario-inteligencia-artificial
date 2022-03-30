from copy import copy

class Particula:
    def __init__(self,x1,x2,vel):
        self.position = [x1,x2]
        self.velocityX1 = vel
        self.velocityX2 = vel
        self.localMemory = copy(self.position)
