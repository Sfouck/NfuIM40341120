import random as rd
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sample = {
    "blue" : 0,
    "green": 0,
    "both" : 0
}

prob = {}

n = 10000

rd.seed(87)

def get_ball():
    return rd.choice(["B","G"])

for _ in range(n):
    ball1 = get_ball()
    ball2 = get_ball()
    if ball1 == "B":
        sample["blue"] += 1
    if ball2 == "G":
        sample["green"] += 1
    if ball1 == "B" and ball2 == "B":
        sample["both"] += 1

for k,v in sample.iteritems():
    prob[k] = 1.0*v / n

print(prob)

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

def normal_two_sided(size,s,a):
    mu, sigma = normal_approximation_to_binomial(size, s)
    print "mu = ", mu
    print "sigma = ", sigma
    print "normal_two_sided_bounds(0.95, mu, sigma) = ", normal_two_sided_bounds(a, mu, sigma)

normal_two_sided(1000,0.5,0.95)
normal_two_sided(1000,0.5,0.9)
normal_two_sided(1000,0.5,0.8)



x = np.linspace(norm.ppf(0.01),norm.ppf(0.99), 100)

plt.plot(x,norm.pdf(x),"r-",lw=2)

r = norm.rvs(size=1000)

plt.hist(r, normed=True, histtype='stepfilled', alpha=0.2)

plt.show()