import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from distributions import OwnUniformDistr, GammaDistribution, NormalDistribution, GeometricDistribution, StudentsDistribution
from distributions import UniformDistr

def normal_distr():
    mu = 0
    sigma = 1

    #g = UniformDistr()
    g = OwnUniformDistr()
    n = NormalDistribution(g, mu, sigma)

    lst = np.array([])
    for i in range(50):
        t = n.next()
        lst = np.append(lst, t)
    print lst
    count, bins, ignored = plt.hist(lst, 30, normed=True)
    plt.plot(bins, stats.norm.pdf(bins, mu, sigma), linewidth=2, color='r')
    plt.xlabel('Probability density function')
    plt.figure(2)
    plt.plot(bins, stats.norm.cdf(bins, mu, sigma), linewidth=2, color='b')
    plt.xlabel('Cumulative distribution function')
    plt.show()

def geom_distr():
    p = 0.35
    g = OwnUniformDistr()
    distr = GeometricDistribution(g, p)
    fig, ax = plt.subplots(1, 1)

    t = []
    for i in range(100):
        t.append(distr.next())

    t = np.sort(np.array(t))
    count, bins, ignored = plt.hist(t, 10, normed=True, color='b')
    plt.xlabel('Probability mass function')

    ax.plot(t, stats.geom.pmf(t, p), 'ro', ms=8, label='geom pmf')
    ax.vlines(t, 0, stats.geom.pmf(t, p), colors='r', lw=5, alpha=0.5)

    plt.figure(2)
    count, bins, ignored = plt.hist(t, 10, normed=True, color='b', cumulative=True)
    plt.plot(bins, stats.geom.cdf(bins, p), linewidth=2, color='r')
    plt.xlabel('Cumulative distribution function')
    plt.show()

def gamma_test():
    v = 5
    g = OwnUniformDistr()
    gamma = GammaDistribution(g, v)
    t = []
    for i in range(100):
        t.append(gamma.next())

    count, bins, ignored = plt.hist(t, 10, normed=True, color='b')
    plt.plot(bins, stats.gamma.pdf(bins, v), linewidth=2, color='r')
    plt.xlabel('Probability density function')
    plt.figure(2)
    count, bins, ignored = plt.hist(t, 10, normed=True, color='b', cumulative=True)
    plt.plot(bins, stats.gamma.cdf(bins, v), linewidth=2, color='r')
    plt.xlabel('Cumulative distribution function')
    plt.show()

def t_distr():
    v = 5
    distr = StudentsDistribution(v)
    v3 = 12
    distr10 = StudentsDistribution(v3)
    t = []
    t10 = []
    for i in range(100):
        t.append(distr.next())
        t10.append(distr10.next())

    x = np.sort(np.array(t))
    x10 = np.sort(np.array(t10))

    p1, = plt.plot(x, stats.t.pdf(x, v), linewidth=2, color='r')
    p2, = plt.plot(x10, stats.t.pdf(x10, v3), linewidth=2, color='b')
    plt.xlabel('Probability density function')
    plt.legend([p1, p2], ['v = 5', "v = 12"])
    plt.figure(2)
    count, bins, ignored = plt.hist(x, 10, normed=True, color='b')
    plt.plot(bins, stats.t.pdf(bins, v), linewidth=2, color='r')
    plt.xlabel('Probability density function')
    plt.figure(3)
    p1, = plt.plot(x, stats.t.cdf(x, v), linewidth=2, color='r')
    p2, = plt.plot(x10, stats.t.cdf(x10, v), linewidth=2, color='b')
    plt.xlabel('Cumulative distribution function')
    plt.legend([p1, p2], ['v = 5', "v = 12"])
    plt.figure(4)
    count, bins, ignored = plt.hist(x, 10, normed=True, color='b', cumulative=True)
    plt.plot(bins, stats.t.cdf(bins, v), linewidth=2, color='r')
    plt.xlabel('Cumulative distribution function')
    plt.show()

geom_distr()