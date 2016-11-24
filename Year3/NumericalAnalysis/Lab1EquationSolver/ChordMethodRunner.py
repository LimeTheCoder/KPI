import numpy as np
from solvers import ChordEquationSolver, SimpleIterationEquationSolver
import Plotter


def f(x):
    return 10. * x - np.sin(np.exp(x)) - x ** 5  + np.exp(np.cos(x)) - np.tan(x)


def first_deriv(x):
    return 10. - 1./np.cos(x) ** 2 - 5 * x ** 4 + \
           np.exp(np.cos(x)) * (-np.sin(x)) - np.exp(x) * np.cos(np.exp(x))


def second_deriv(x):
    return -20. * x ** 3 - 2 * np.tan(x) * (1. + np.tan(x) ** 2) + \
           np.exp(np.cos(x)) * (np.sin(x) ** 2 - np.cos(x)) - \
           np.exp(x) * np.cos(np.exp(x)) + np.exp(2 * x) * np.sin(np.exp(x))

a = -1
b = 1

print 'Left: %d, Right: %d' % (a, b)
print 'f(left): %d, f(right): %d' % (f(a), f(b))
print 'first_der(left): %d, first_der(right): %d' % (first_deriv(a), first_deriv(b))
print 'second_der(left): %d, second_der(right): %d' % (second_deriv(a), second_deriv(b))

x1, hist1 = ChordEquationSolver.solve(a, b, 0.001, f, first_deriv, second_deriv)
x, hist = SimpleIterationEquationSolver.solve(a, b, 0.001, f, first_deriv)

Plotter.plot_history(hist, "Simple iteration method")
Plotter.plot_history(hist1, 'Chord method')
print 'Root: ', x, x1