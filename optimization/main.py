import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ABC import ABC
from copy import deepcopy

from matplotlib.style import use

from function import eggholderV3, eggholderV2


use('classic')
df = pd.DataFrame()


def get_objective(objective, dimension=2):
    objectives = {'EggHolder': eggholderV3(dimension)}
    return objectives[objective]


def simulate(obj_function, colony_size=200, n_iter=50, max_trials=100, simulations=100):
    itr = range(n_iter)
    values = np.zeros(n_iter)
    box_optimal = []

    sum = 0
    avg = [0]
    best = None
    for _ in range(simulations):
        optimizer = ABC(obj_function=get_objective(obj_function), colony_size=colony_size, n_iter=n_iter,
                        max_trials=max_trials)
        optimizer.optimize()
        values += np.array(optimizer.optimality_tracking)
        box_optimal.append(optimizer.optimal_solution.fitness)

        cur = optimizer.getCurrentSolution()
        if not best or cur.fitness < best.fitness:
            best = deepcopy(cur)

        sum += optimizer.optimal_solution.fitness
        avg.append(sum / len(avg))

    print(best.fitness, best.pos)

    values /= simulations

    df[obj_function] = box_optimal
    plt.plot(avg, color="blue")


def main():
    global df

    plt.figure(figsize=(10, 7))
    df = pd.DataFrame()
    simulate('EggHolder')

    plt.ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    plt.xticks(rotation=45)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Fitness Value')
    # plt.savefig('abc_rast.jpg')
    # df.to_csv('abc_sphere.csv')
    plt.show()


if __name__ == '__main__':
    main()
