import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ABC import ABC

from matplotlib.style import use

from function import eggholderV3, eggholderV2


use('classic')
df = pd.DataFrame()


def get_objective(objective, dimension=30):
    objectives = {'EggHolder': eggholderV3(dimension)}
    return objectives[objective]


def simulate(obj_function, colony_size=30, n_iter=5000, max_trials=100, simulations=1):
    itr = range(n_iter)
    values = np.zeros(n_iter)
    box_optimal = []
    for _ in range(simulations):
        optimizer = ABC(obj_function=get_objective(obj_function), colony_size=colony_size, n_iter=n_iter,
                        max_trials=max_trials)
        optimizer.optimize()
        values += np.array(optimizer.optimality_tracking)
        box_optimal.append(optimizer.optimal_solution.fitness)
        print(optimizer.optimal_solution.pos)
    values /= simulations

    df[obj_function] = box_optimal
    plt.plot(itr, values, lw=0.5, label=obj_function)
    plt.legend(loc='upper right')


def main():
    global df

    plt.figure(figsize=(10, 7))
    df = pd.DataFrame()
    simulate('EggHolder')


    plt.ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    plt.xticks(rotation=45)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Fitness Value')
    #plt.savefig('abc_rast.jpg')
    # df.to_csv('abc_sphere.csv')
    plt.show()


if __name__ == '__main__':
    main()
