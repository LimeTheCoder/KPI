from Generators import FibonacciGenerator
import numpy as np


# Standart uniform distribution from math package
class UniformDistr:

    def next(self, num=1):
        return np.random.rand(num)


class OwnUniformDistr:
    def __init__(self):
        self.__f = FibonacciGenerator(23, 10, 13)

    def next(self, cnt=1):
        nums = []
        for i in range(cnt):
            nums.append(self.__f.next())
        return np.array(nums)


class NormalDistribution:

    def __init__(self, uniform_gen, mu, sigma):
        self.__g = uniform_gen
        self.__mu = mu
        self.__sigma = sigma

    def next(self):
        while True:
            u = self.__g.next(2)
            v = 2 * u - 1
            s = sum(map(lambda x: x * x, v))

            if s < 1:
                x = v * np.sqrt(-2 * np.log(s) / s)
                x = self.__mu + self.__sigma * x
                return x


class GeometricDistribution:
    def __init__(self, uniform_gen, p):
        self.__p = p
        self.__g = uniform_gen

    def next(self):
        return int(np.log(self.__g.next()) / np.log(1 - self.__p))


class GammaDistribution:

    def __init__(self, uniform_gen, alpha):
        self.__alpha = alpha
        self.__g = uniform_gen

    def next(self):
        while True:
            y = np.tan(np.pi * float(self.__g.next()))
            x = np.sqrt(2 * self.__alpha - 1) * y + self.__alpha - 1
            if x > 0:
                v = float(self.__g.next())
                if v <= (1 + y**2) * np.exp((self.__alpha - 1) * np.log(x / (self.__alpha - 1.)) - np.sqrt(2 * self.__alpha - 1) * y):
                    return x


class Chi2Distribution:

    def __init__(self, v):
        self.__v = v
        self.__g = GammaDistribution(OwnUniformDistr(), v/2)

    def next(self):
        return 2 * self.__g.next()


class StudentsDistribution:
    def __init__(self, v):
        self.__v = v
        self.__ngen = NormalDistribution(OwnUniformDistr(), 0, 1)
        self.__chigen = Chi2Distribution(v)

    def next(self):
        y1 = float(self.__ngen.next()[0])
        y2 = float(self.__chigen.next())

        return y1 / np.sqrt(y2 / self.__v)
