from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# constantes del problema
DIMENSIONS = 2  # número de dimensiones
BOUND_LOW, BOUND_UP = -512.0, 512.0  # limites de todas las dimensiones

# constantes del algoritmo gentico
POPULATION_SIZE = 300
P_CROSSOVER = 0.9  # probabilidad de cruzarse
P_MUTATION = 0.1
MAX_GENERATIONS = 300
HALL_OF_FAME_SIZE = 30
CROWDING_FACTOR = 20.0

# ponerle la semilla aleatoria
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

# definir un único objetivo, minimizando la estrategia de aptitud
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create la clase del Individuo basado en la lista:
creator.create("Individual", list, fitness=creator.FitnessMin)


# asume que el rango es el mismo para cada dimensión
def randomFloat(low, up):
    return [random.uniform(l, u) for l, u in zip([low] * DIMENSIONS, [up] * DIMENSIONS)]


# create operador que aleatoriamente regresa un float en el rango deseado y dimensión
toolbox.register("attrFloat", randomFloat, BOUND_LOW, BOUND_UP)

# create the individual operator to fill up an Individual instance:
toolbox.register(
    "individualCreator", tools.initIterate, creator.Individual, toolbox.attrFloat
)

# crear el operador de población para generar una lista de individuos
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# Función eggolder para la aptitud de cada individuo
def eggholder(individual):
    x = individual[0]
    y = individual[1]
    f = -(y + 47.0) * np.sin(np.sqrt(abs(x / 2.0 + (y + 47.0)))) - x * np.sin(
        np.sqrt(abs(x - (y + 47.0)))
    )
    return (f,)  # return a tuple


toolbox.register("evaluate", eggholder)

# operadores genéticos
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register(
    "mate",
    tools.cxSimulatedBinaryBounded,
    low=BOUND_LOW,
    up=BOUND_UP,
    eta=CROWDING_FACTOR,
)
toolbox.register(
    "mutate",
    tools.mutPolynomialBounded,
    low=BOUND_LOW,
    up=BOUND_UP,
    eta=CROWDING_FACTOR,
    indpb=1.0 / DIMENSIONS,
)


# flujo del algoritmo genético
def main():

    # crear población inicial
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # preparar objeto estadístico
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    # definir objecto hall-of-fame
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # crear el algoritmo de flujo del algoritmo genético
    population, logbook = algorithms.eaSimple(
        population,
        toolbox,
        cxpb=P_CROSSOVER,
        mutpb=P_MUTATION,
        ngen=MAX_GENERATIONS,
        stats=stats,
        halloffame=hof,
        verbose=True,
    )

    # imprimir la mejor solución
    best = hof.items[0]
    print("-- Best Individual = ", best)
    print("-- Best Fitness = ", best.fitness.values[0])

    # extraer estadísticas
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    # graficar estadísticas
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color="red")
    plt.plot(meanFitnessValues, color="green")
    plt.xlabel("Generation")
    plt.ylabel("Min / Average Fitness")
    plt.title("Min and Average fitness over Generations")

    plt.show()


if __name__ == "__main__":
    main()
