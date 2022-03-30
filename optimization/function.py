import numpy as np

# Función eggholder


def eggholder(x, y):
    return -(y + 47.0) * np.sin(np.sqrt(abs(x / 2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0))))


def eggholderV2(x):
    term1 = -(x[1]+47) * np.sin(np.sqrt(np.fabs(x[1]+x[0]/2+47)))
    term2 = -x[0] * np.sin(np.sqrt(np.fabs(x[0]-(x[1]+47))))
    result = term1 + term2
    return result
