import numpy as np

# Función eggholder
def eggholder(x, y):
    return -(y + 47.0) * np.sin(np.sqrt(abs(x / 2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0))))
