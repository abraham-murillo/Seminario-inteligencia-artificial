import numpy as np
from abc import ABCMeta
from abc import abstractmethod
from six import add_metaclass

# Función eggholder


def eggholder(x, y):
    return -(y + 47.0) * np.sin(np.sqrt(abs(x / 2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0))))


def eggholderV2(x):
    term1 = -(x[1]+47) * np.sin(np.sqrt(np.fabs(x[1]+x[0]/2+47)))
    term2 = -x[0] * np.sin(np.sqrt(np.fabs(x[0]-(x[1]+47))))
    result = term1 + term2
    return result

@add_metaclass(ABCMeta)
class ObjectiveFunction(object):

    def __init__(self, name, dim, minf, maxf):
        self.name = name
        self.dim = dim
        self.minf = minf
        self.maxf = maxf

    def sample(self):
        return np.random.uniform(low=self.minf, high=self.maxf, size=self.dim)

    def custom_sample(self):
        return np.repeat(self.minf, repeats=self.dim) \
               + np.random.uniform(low=0, high=1, size=self.dim) *\
               np.repeat(self.maxf - self.minf, repeats=self.dim)

    #@abstractmethod
    #def evaluate(self, x):
    #    pass

class eggholderV3(ObjectiveFunction):

    def __init__(self, dim):
        super(eggholderV3, self).__init__('EggHolder', dim, -512, 512)

    def evaluate(self, x):
        return (-(x[1] + 47) * np.sin(np.sqrt(abs(x[0]/2 + (x[1] + 47)))) -x[0] * np.sin(np.sqrt(abs(x[0] - (x[1] + 47)))))
