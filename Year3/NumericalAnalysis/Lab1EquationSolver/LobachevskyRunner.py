from solvers import AlgebraicEquationSolver
import numpy as np
import matplotlib.pyplot as plt

def algebraic_function(coeff, x):
    res = 0.
    for i in range(len(coeff)):
        res += coeff[i] * x ** (len(coeff) - 1. - i)
    return res

coeff = np.array([2, 48, -67, -722, -141, 988, -288, -14]) / 988.
#coeff = [1, -35, 380, -1350, 1000]
#s = raw_input()
#coeff = map(int, s.split())

roots, errors_hist = AlgebraicEquationSolver.solve(coeff, 0.001)
print 'Roots:'
print roots
print 'f(x):'
print algebraic_function(coeff, roots)

plt.style.use('ggplot')
plt.title('Lobachevsky method', fontname='Ubuntu', fontsize=16,
          fontstyle='italic', fontweight='bold')

plt.plot(list(range(len(errors_hist[1:]))), errors_hist[1:], linewidth=2.0)
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.show()