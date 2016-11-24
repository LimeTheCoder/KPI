import numpy as np


def solve(coefficients, epsilon):
    length = len(coefficients)
    original = np.array(coefficients)
    old_coeff = np.array(coefficients)
    new_coeff = np.array([])

    p = 0

    errors_hist = []

    while True:
        for i in range(length):
            tmp = old_coeff[i] ** 2.
            j = 1
            while i - j >= 0 and i + j < length:
                val = 2 * old_coeff[i - j] * old_coeff[i + j]
                if j % 2 == 1: val *= -1
                tmp += val
                j += 1

            new_coeff = np.append(new_coeff, tmp)

        p += 1
        error = np.max(np.abs(1. - new_coeff / old_coeff ** 2.))

        print 'Iteration: ', p
        print 'Error: ', error
        print 'Coeff:'
        print new_coeff

        errors_hist.append(error)
        if error <= epsilon: break

        old_coeff = new_coeff.copy()
        new_coeff = np.array([])

    roots = np.array([])

    for k in range(1, length):
        root = new_coeff[length - k] / new_coeff[length - k - 1]
        power = 2. ** p
        root **= (1. / power)
        s = -np.sign(original[length - k] / original[length - k - 1])
        roots = np.append(roots, root * s)

    return roots, errors_hist