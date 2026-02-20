import random
import math
import matplotlib.pyplot as plt

# To see the same results
random.seed(21)

def buffons_needle(iter, l, d):
    crossed = 0
    for _ in range(iter):
        angle = random.uniform(0, math.pi/2)
        half_dist = random.uniform(0, d/2)

        if (half_dist <= (l/2)*math.sin(angle)):
            crossed += 1
    return crossed/iter

def monte_carlo_pi(iter, l, d):
    probability = buffons_needle(iter, l, d)

    if probability == 0:
        return None

    return (2 * l) / (d * probability)

def run_experiment():
    iters = []
    pi_hats = []
    pi_errors = []

    for d in range(2, 4):
        for L in range(1, d):
            for i in range(2, 7):
                n_iter = 10**i
                est_prob = buffons_needle(n_iter, L, d)
                est_pi = monte_carlo_pi(n_iter, L, d)

                
                print("---------------------")
                print("Iteration Number: ", n_iter)
                print("Length of Needle: ", L, " |  Distance Between Lines: ", d)
                print("Estimated Probability:", est_prob)
                print("Estimated Pi:", est_pi)
                print("---------------------")

                if est_pi is not None and L == 1 and d == 2:
                    iters.append(n_iter)
                    pi_hats.append(est_pi)
                    pi_errors.append(abs(math.pi - est_pi))

    plt.figure()
    plt.plot(iters, pi_errors, marker="o")
    plt.xlabel("Iteration count n")
    plt.ylabel("Absolute error")
    plt.grid(True, which="both")
    plt.show()
