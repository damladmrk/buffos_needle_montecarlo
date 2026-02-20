import random
import math
import matplotlib.pyplot as plt

# To see the same results
random.seed(21)

def buffons_needle(iter, l, d):
    """
    Simulates Buffon's Needle experiment for parallel lines.

    Params:
    iter : number of needle drops
    l    : needle length (L < D)
    d    : distance between parallel lines

    Returns:
    Estimated crossing probability P.
    """
    crossed = 0
    for _ in range(iter):
        angle = random.uniform(0, math.pi/2)
        half_dist = random.uniform(0, d/2)

        if (half_dist <= (l/2)*math.sin(angle)):
            crossed += 1
    return crossed/iter

def monte_carlo_pi(iter, l, d):
    """
    Estimates π using the Buffon's Needle probability formula:
        Pi ≈ 2L / (D * P)
    Returns:
    Estimated Pi value.
    """
    probability = buffons_needle(iter, l, d)

    if probability == 0:
        return None

    return (2 * l) / (d * probability)

def run_experiment():
    true_pi = math.pi
    iters = []
    pi_hats = []
    prob_hats = []
    pi_errors = []

    ratio_data = {}  # key = L/D, value = (iters, pi_errors)

    for d in range(2, 4):
        for L in range(1, d):
            ratio = L/d
            if ratio not in ratio_data:
                ratio_data[ratio] = ([], [])

            for i in range(2, 7):
                n_iter = 10**i
                est_prob = buffons_needle(n_iter, L, d)
                est_pi = monte_carlo_pi(n_iter, L, d)
                
                print("-" * 60)
                print("Iteration Number: ", n_iter)
                print("Length of Needle: ", L, " |  Distance Between Lines: ", d)
                print("Estimated Probability:", est_prob)
                print("Estimated Pi:", est_pi)
                print("-" * 60)
                
                if est_pi is not None:
                    ratio_data[ratio][0].append(n_iter)
                    ratio_data[ratio][1].append(abs(math.pi - est_pi))


                if est_pi is not None and L == 1 and d == 2:
                    iters.append(n_iter)
                    pi_hats.append(est_pi)
                    pi_errors.append(abs(math.pi - est_pi))

    # Error by Iteration Graph
    plt.figure()
    plt.plot(iters, pi_errors, marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Iteration count n")
    plt.ylabel("Absolute error")
    plt.grid(True, which="both")
    plt.show()

    # Pi Convergence Graph
    plt.figure()
    plt.plot(iters, pi_hats, marker="o")
    plt.axhline(true_pi, linestyle="--")
    plt.xscale("log")
    plt.xlabel("Iteration count n")
    plt.ylabel("Estimated Pi")
    plt.title("Pi Convergence (L=1, D=2)")
    plt.grid(True, which="both")
    plt.show()

    # Graphs by Different L/D Ratios
    plt.figure()
    for ratio, (n_vals, err_vals) in ratio_data.items():
        plt.plot(n_vals, err_vals, marker="o", label=f"L/D={ratio:.2f}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Iteration count n")
    plt.ylabel("Absolute error of Pi")
    plt.title("Error Comparison for Different L/D Ratios")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()
