import numpy as np


def solve(left, right, epsilon, f, first_deriv, second_deriv):
    if f(left) * f(right) > 0:
        return None

    xk = left if f(left) * second_deriv(left) > 0 else right
    h = 1. / first_deriv(xk)

    print 'h: ', h

    m = np.abs(first_deriv(left))

    for i in np.arange(left, right, epsilon):
        val = np.abs(first_deriv(i))
        if val < m: m = val

    print 'm: ', m

    history = [xk]

    while (np.abs(f(xk)) / m) > epsilon:
        xk -= f(xk) * h
        print 'xk: ', xk
        history.append(xk)

    return xk, history