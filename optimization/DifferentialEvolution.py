import random
import numpy as np
from function import eggholderV2
import matplotlib.pyplot as plt


def func1(x):
    # Sphere function, use any bounds, f(0,...,0)=0
    return sum([x[i]**2 for i in range(len(x))])


def ensure_bounds(vec, bounds):
    vec_new = []
    # cycle through each variable in vector
    for i in range(len(vec)):

        # variable exceedes the minimum boundary
        if vec[i] < bounds[i][0]:
            vec_new.append(bounds[i][0])

        # variable exceedes the maximum boundary
        if vec[i] > bounds[i][1]:
            vec_new.append(bounds[i][1])

        # the variable is fine
        if bounds[i][0] <= vec[i] <= bounds[i][1]:
            vec_new.append(vec[i])

    return vec_new


def differentialEvolution(cost_func, bounds, popsize, mutate, recombination, maxiter, p):
    archived = []
    population = []
    values = []

    for i in range(0, popsize):
        indv = []
        for j in range(len(bounds)):
            indv.append(random.uniform(bounds[j][0], bounds[j][1]))
        population.append(indv)
        values.append(cost_func(indv))
    # print(population)

    evaluation = []
    average = []

    # cycle through each generation (step #2)
    for i in range(0, maxiter):
        print("Generation:", i)
        # print(population)
        pop_sort = []
        combined = []
        for k in population:
            combined.append(k)
        if(i > 1):
            pop_sort = np.column_stack((population, gen_scores))
            pop_sort = pop_sort[pop_sort[:, len(bounds)].argsort()]
            pop_sort = np.delete(pop_sort, len(bounds), 1)
            for k in archived:
                combined.append(k)
            # print(pop_sort)
            # print(combined)
        else:
            pop_sort = np.column_stack((population, values))
            pop_sort = pop_sort[pop_sort[:, len(bounds)].argsort()]
            pop_sort = np.delete(pop_sort, len(bounds), 1)

        gen_scores = []  # score keeping
        # print(gen_scores)
        s_f = []
        s_cr = []
        cr = []
        f = []
        # cycle through each individual in the population
        for j in range(0, popsize):
            for k in archived:
                combined.append(k)
            # Mutation
            # select three random vector index positions [0, popsize), not including current vector (j)
            cr_list = (np.arange(0.1, recombination+1, 0.01))
            f_list = (np.arange(0.1, mutate+1, 0.01))
            # print(cr_list, f_list)
            cr.append(np.random.choice(cr_list))
            f.append(np.random.choice(f_list))

            candidates1 = list(np.arange(0, int(100*p)).astype(np.int64))
            candidates2 = list(range(0, popsize))
            candidates3 = list(range(0, len(archived)+popsize))
            # print(len(candidates3))
            candidates2.remove(j)
            candidates3.remove(j)

            #random_index = random.sample(canidates, 2)
            x_1 = pop_sort[np.random.choice(candidates1)]
            x_2 = population[np.random.choice(candidates2)]
            x_3 = combined[np.random.choice(candidates3)]
            x_t = population[j]     # target individual

            # subtract x3 from x2, and create a new vector (x_diff)
            x_diff1 = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
            x_diff2 = [x_1_i - x_t_i for x_1_i, x_t_i in zip(x_1, x_t)]
            # multiply x_diff by the mutation factor (F) and add to x_1
            v_donor = [x_t_i + mutate * x_diff1_i+mutate*x_diff2_i for x_t_i,
                       x_diff1_i, x_diff2_i in zip(x_t, x_diff1, x_diff2)]
            v_donor = ensure_bounds(v_donor, bounds)

            # Recombination
            j_rand = random.randint(1, len(x_t))
            # print(cr[j])
            v_trial = []
            for k in range(len(x_t)):
                # crossover = random.random()
                if k == j_rand or random.uniform(0, 1) < cr[j]:
                    v_trial.append(v_donor[k])

                else:
                    v_trial.append(x_t[k])

            # Greedy selection
            score_trial = cost_func(v_trial)
            score_target = cost_func(x_t)

            if score_trial < score_target:
                population[j] = v_trial
                archived.append(x_t)
                s_cr.append(cr[j])
                s_f.append(f[j])

                gen_scores.append(score_trial)
                # print('   >', score_trial, v_trial)

            else:
                # print('   >', score_target, x_t)
                gen_scores.append(score_target)
            if(len(archived) > popsize):
                r = random.randrange(0, len(archived), 1)
                del archived[r]

        c = random.uniform(0, 1)
        sqsumf = 0
        sumf = 0
        for k in s_f:
            sqsumf += k*k
            sumf += k

        if sumf == 0:
            mean_l = 0
        else:
            mean_l = sqsumf/sumf

        recombination = (1-c)*recombination+c*np.mean(s_cr)
        mutate = (1-c)*mutate+c*mean_l

        # Score keeping
        # current generation avg. fitness
        gen_avg = sum(gen_scores) / popsize
        # fitness of best individual
        gen_best = min(gen_scores)
        # solution of best individual
        gen_sol = population[gen_scores.index(min(gen_scores))]

        print(' Average: ', gen_avg)
        print(' Best: ', gen_best)
        print(' Best solution:', gen_sol, '\n')

        evaluation.append(gen_best)
        average.append(gen_avg)

    plt.plot(evaluation, color="blue")
    plt.plot(average, color="red")
    plt.xlabel("Iterations")
    plt.ylabel("Min/ average")
    plt.title("Average fitness over iterations")
    plt.show()


# Cost function
cost_func = eggholderV2
# Bounds [(x1_min, x1_max), (x2_min, x2_max),...]
bounds = [(-512, 512), (-512, 512)]
# Population size, must be >= 4
popsize = 100
# Mutation factor [0,2]
mutate = 0.5
# Recombination rate [0,1]
recombination = 0.5
# Max number of generations (maxiter)
maxiter = 100
p = 0.05

differentialEvolution(cost_func, bounds, popsize,
                      mutate, recombination, maxiter, p)
