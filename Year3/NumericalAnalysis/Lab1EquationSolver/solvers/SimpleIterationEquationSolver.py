import numpy as np


class Reflector:
    def __init__(self, f, first_der):
        self.f = f
        self.first_der = first_der

    def reflected_function(self, x):
        return -self.f(x)

    def reflected_first_der(self, x):
        return -self.first_der(x)


def get_phi(f, l):
    def phi(x):
        return x - l * f(x)
    return phi


def solve(left, right, epsilon, f, first_deriv):
    if f(left) * f(right) > 0 \
            or first_deriv(left) * first_deriv(right) <= 0:
        return None

    if first_deriv(left) < 0:
        r = Reflector(f, first_deriv)
        f = r.reflected_function
        first_deriv = r.reflected_first_der

    alpha = first_deriv(left)
    gamma = first_deriv(left)

    for i in np.arange(left, right, epsilon):
        if first_deriv(i) < alpha: alpha = first_deriv(i)
        if first_deriv(i) > gamma: gamma = first_deriv(i)

    q = (gamma - alpha) / (gamma + alpha)
    l = 2. / (alpha + gamma)
    phi = get_phi(f, l)

    print 'alpha: ', alpha
    print 'gamma: ', gamma
    print 'q: ', q

    xk = (left + right) / 2.
    iteration = 1
    hist = [xk]

    while True:
        x_prev = xk
        xk = phi(x_prev)
        print 'Iteration: ', iteration
        print 'xk: ', xk
        hist.append(xk)

        if np.abs(xk - x_prev) <= (1. - q) / q * epsilon: break

        iteration += 1

    return xk, hist