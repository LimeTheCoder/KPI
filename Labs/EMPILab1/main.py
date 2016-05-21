from Generators import MauchlyGenerator, FibonacciGenerator, linear_congruential_method, InvCongruentialGenerator, BaysDurhamGenerator
from Generators import Super_Generator
import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

from tests import get_partition_theor


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


def linear_test1():
    m = 6075
    a = 106
    c = 1283
    s = set()
    curr = 103
    cnt = 0

    while curr not in s:
        s.add(curr)
        curr = linear_congruential_method(m, a, c, curr)
        cnt +=1
        print curr, cnt

    b = a - 1
    potential(b, m)


def linear_test2():
    num = 7
    m = 6100
    a = 104
    c = 1300

    s = set()
    cnt = 0

    while num not in s:
        s.add(num)
        num = linear_congruential_method(m, a, c, num)
        cnt += 1
        print num, cnt



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
    for i in range(5):
        y.append(partition.count(i + 1))
    y = np.array(y)
    v = sum((y - theor) ** 2 / theor.astype(float))
    return v

#g = InvCongruentialGenerator(5, 2, 3, 1)
#print partition_criterion(g, 5, 5, 1000)
#g = BaysDurhamGenerator()
#print partition_criterion(g, 50, 5, 1000)
g = Super_Generator(10, 5, 2, 7)
print partition_criterion(g, 10, 5, 1000)