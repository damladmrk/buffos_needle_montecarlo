import random
import math

# To see the same results
random.seed(21)

def buffons_needle(L, D, R):
    u = random.random()
    # Since creating a random point in the radial direction uniformly is hard to achive,
    # I scaled the initial variable according to my space
    r = R * math.sqrt(u)
    angle = random.uniform(0.0, 2.0 * math.pi)
    center_x, center_y = r * math.cos(angle), r * math.sin(angle)

    theta = random.uniform(0.0, 2.0 * math.pi)
    hx = (L / 2.0) * math.cos(theta)
    hy = (L / 2.0) * math.sin(theta)

    # The end points of the rod
    x1, y1 = center_x - hx, center_y - hy
    x2, y2 = center_x + hx, center_y + hy

    # Distances to the origin of the end points
    rho1 = math.hypot(x1, y1)
    rho2 = math.hypot(x2, y2)

    # I am checking that if the end points are squeezing one of D
    k1 = int(rho1 // D)
    k2 = int(rho2 // D)

    return k1 != k2


def monte_carlo_probability(n, L, D, R):
    crossed = 0
    for _ in range(n):
        if buffons_needle(L, D, R):
            crossed += 1
    return crossed / n


def p_theory(L, D):
    return (2.0 * L) / (math.pi * D)


def pi_from_p(P, L, D):
    return (2.0 * L) / (P * D)


def run_experiments():
    n = 200_000            
    R_mult = 400            
    D_list = [1.0, 2.0, 5.0]
    L_list = [0.5, 0.75, 1.0, 2.0] 
    print("-" * 90)

    for D in D_list:
        R = R_mult * D
        for L in L_list:
            if not (L < D):
                continue

            P_mc = monte_carlo_probability(n, L, D, R)
            P_th = p_theory(L, D)

            pi_mc = pi_from_p(P_mc, L, D)
            pi_err = abs(pi_mc - math.pi)
            p_err = abs(P_mc - P_th)

            print(
                f"D={D:>4.1f}  L={L:>5.3f} | "
                f"P from Monte Carlo={P_mc:>8.6f}  P Theory={P_th:>8.6f} | "
                f"Pi from Monte Carlo={pi_mc:>8.6f}  Pi Error={pi_err:>8.6f}"
            )
        print("-" * 90)
