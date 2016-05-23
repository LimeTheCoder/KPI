from Generators import MauchlyGenerator, FibonacciGenerator, LinearCongruentialGenerator, InvCongruentialGenerator, BaysDurhamGenerator
from Generators import Super_Generator
import numpy as np
from scipy.special import gamma
from scipy import stats
import matplotlib.pyplot as plt

from tests import get_partition_theor, coupon_practic, coupon_theor


def mauchly_test():
    generator = MauchlyGenerator('1234012340123', 5)
    s = set()
    curr = 0
    while curr not in s:
        s.add(curr)
        curr = generator.next()

    print len(s)


def potential(b, m):
    p = 1
    while (b ** p) % m != 0:
        p += 1
    print "P : " + str(p)


def fibonacci_test():
    f = FibonacciGenerator(16, 10, 7) # good test
    num = f.next()
    cnt = 0
    while cnt != 50:
        cnt += 1
        next_num = f.next()
        print next_num, cnt


def inv_cong_test():
    g = InvCongruentialGenerator(5, 2, 3, 1)
    for i in range(50):
        print g.next()


def bays_durkham_test():
    g = BaysDurhamGenerator()
    for i in range(50):
        print g.next()


def own_method_test():
    gen = Super_Generator(10, 5, 2, 7)
    gen.next()
    a = 5
    b = 2
    c = 7
    cnt = 1
    while True:
        if gen.a == a and gen.b == b and gen.c == c:
            break
        cnt += 1
        print gen.next()
    print cnt


def stirling_gamma(z):
    return np.sqrt(2.0 * np.pi / z) * (z / np.exp(1)) ** z


def gamma_distr_dens(x, k=2.0, theta=2.0, gamma_to_run = gamma):
    return x**(k-1) * np.exp(-x/theta) / (gamma_to_run(k) * theta ** k)


def gamma_test():
    x = np.linspace(0.05, 2, 40)
    zs = stirling_gamma(x)
    zn = gamma(x)

    p1, = plt.plot(x, zs, 'r')
    p2, = plt.plot(x, zn, 'b')
    plt.legend([p1, p2], ['Stirling approximation', "Numpy realization"])

    x = np.linspace(0.05, 10, 200)

    plt.figure(2)
    p1, = plt.plot(x, gamma_distr_dens(x, gamma_to_run=stirling_gamma), 'r', )
    p2, = plt.plot(x, gamma_distr_dens(x), 'b')
    plt.legend([p1, p2], ['Stirling approximation', "Numpy realization"])
    plt.show()


def chi2_criterion(practic, theor, k):
    v = sum((practic - theor) ** 2 / theor.astype(float))
    return v, 1 - stats.chi2.cdf(v, k)

def partition_criterion(g, m, k, w):
    theor = get_partition_theor(m, k) * w

    generated_lists = []
    for i in range(w):
        list_of_k = []
        for j in range(k):
            list_of_k.append(g.next())
        generated_lists.append(list_of_k)
    partition = [len(set(lst)) for lst in generated_lists]
    y = []
    for i in range(k):
        y.append(partition.count(i + 1))
    y = np.array(y)
    print theor, y
    return chi2_criterion(practic=y, theor=theor, k=k)

def coupon_criterion(g, d, n):
    theor = []
    t = 3 * d
    for i in range(t - d):
        theor.append(coupon_theor(d, d + i))
    theor.append(coupon_theor(d=d, t=t, compute_for_t=True))
    theor = np.array(theor) * n

    practical = coupon_practic(g, t, d, n)
    print theor
    print practical
    k = t - d + 1
    return chi2_criterion(practic=practical, theor=theor, k=k)

#g = InvCongruentialGenerator(5, 2, 3, 1)
#print coupon_criterion(g, 5, 100)
#print partition_criterion(g, 5, 5, 1000)
#g = BaysDurhamGenerator()
#print partition_criterion(g, 50, 5, 1000)
#g = Super_Generator(10, 5, 2, 7)
#print coupon_criterion(g, 10, 100)
#print partition_criterion(g, 10, 5, 10)
#g = LinearCongruentialGenerator(7875, 211, 1663, 7)
#print partition_criterion(g, 7875, 5, 1000)
#g = LinearCongruentialGenerator(7, 4, 3, 7)
#print coupon_criterion(g, 7, 10)