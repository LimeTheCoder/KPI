import numpy as np


def solve(left, right, epsilon, f, first_deriv, second_deriv):
    if f(left) * f(right) > 0\
            or first_deriv(left) * first_deriv(right) <= 0:
        return None

    if f(left) * second_deriv(left) > 0:
        c = left
        xk = right
    else:
        c = right
        xk = left

    print 'c:', c
    print 'x0: ', xk

    hist = [xk]

    m = np.abs(first_deriv(left))

    for i in np.arange(left, right, epsilon):
        val = np.abs(first_deriv(i))
        if val < m: m = val

    cnt = 1
    while (np.abs(f(xk)) / m) > epsilon:
        xk -= f(xk) / (f(xk) - f(c)) * (xk - c)
        print 'Iteration: ', cnt
        print 'xk: ', xk
        hist.append(xk)
        cnt += 1

    return xk, hist