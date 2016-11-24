from solvers import NewtonSiplifiedEquationSolver
import numpy as np
import Plotter

def f(x):
    return x ** 3. * np.cos(x) + np.pi - 9. * np.pi * x


def first_deriv(x):
    return 3. * x ** 2 - x ** 3 * np.sin(x) - 9 * np.pi


def second_deriv(x):
    return x * np.cos(x) * (6. - x ** 2) - 6. * x ** 2 * np.sin(x)

'''
def f(x):
    return x ** 3. - 18. * x - 83.


def first_deriv(x):
    return 3. * x ** 2 - 18.

def second_deriv(x):
    return 6. * x
'''


x, hist = NewtonSiplifiedEquationSolver.solve(-2, 2, 0.00001, f, first_deriv, second_deriv)
print f(x), x

Plotter.plot_history(hist, "Newton Simplified Method")

print hist