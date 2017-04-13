from __future__ import division
from funcs import *


if __name__ == "__main__":

    print "using the gradient"

    v = [random.randint(-10, 10) for i in range(3)]
    count = 0

    tolerance = 0.0000001


    while True:
        # print v, sum_of_squares(v)
        gradient = sum_of_squares_gradient(v)  # compute the gradient at v
        next_v = step(v, gradient, -0.1)  # take a negative gradient step
        print(str(count) + "," + str(next_v))
        count += 1
        if distance(next_v, v) < tolerance:  # stop if we're converging
            break
        v = next_v  # continue if we're not

    print "minimum v", v
    print "minimum value", sum_of_squares(v)
    print

    print "using minimize_batch"

    v = [random.randint(-10, 10) for i in range(3)]

    v = minimize_batch(sum_of_squares, sum_of_squares_gradient, v)

    print "minimum v", v
    print "minimum value", sum_of_squares(v)
