class MauchlyGenerator:
    def __init__(self, seed, base):
        self.__history = []
        self.__base = base
        self.__dig_cnt = len(seed)

        num = int(seed, 5)
        for i in range(6):
            num = self.__neumann_method(num, num)
            self.__history.insert(0, num)

    def __to_base(self, num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
        return ((num == 0) and numerals[0]) or (self.__to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

    def __neumann_method(self, m, n):
        res = self.__to_base(m * n, self.__base).zfill(self.__dig_cnt * 2)
        return int(res[(self.__dig_cnt / 2) : (3 * self.__dig_cnt / 2)], self.__base)

    def next(self):
        next_num = self.__neumann_method(self.__history[0], self.__history.pop())
        self.__history.insert(0, next_num)
        return self.__to_base(next_num, self.__base)


class FibonacciGenerator:
    def __init__(self, k, m, seed):
        self.__history = []
        self.__m = m
        num = seed
        for i in range(k):
            num = linear_congruential_method(6075, 106, 1283, num)
            self.__history.insert(0, num)

    def next(self):
        next_num = (self.__history[0] + self.__history.pop()) % self.__m
        self.__history.insert(0, next_num)
        return next_num


class InvCongruentialGenerator:
    def __init__(self, p, a, c, seed):
        self.__p = p
        self.__a = a
        self.__c = c
        self.__x = seed

    def next(self):
        if self.__x == 0:
            self.__x = self.__c
            return self.__c
        try:
            self.__x = (self.__a * inv(self.__x, self.__p) + self.__c) % self.__p
        except:
            raise Exception("Inverse number doesn't exist")
        return self.__x


class BaysDurhamGenerator:
    def __init__(self):
        self.__table = []
        self.__k = 50
        self.__m = 83
        num = 7
        for i in range(self.__k):
            num = linear_congruential_method(self.__m, 12, 7, num)
            self.__table.append(num)
        self.__y = linear_congruential_method(self.__m, 12, 7, num)

    def next(self):
        j = self.__k * self.__y / self.__m
        self.__y = linear_congruential_method(self.__m, 12, 7, self.__y)
        x = self.__table[j]
        self.__table[j] = self.__y
        return x


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def inv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def linear_congruential_method(m, a, c, x):
    return (a * x + c) % m


class Super_Generator:
    def __init__(self, m, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.m = m

    def next(self):
        res = (self.a ** 3 + self.b ** 2 + self.c) % self.m
        self.a = self.b
        self.b = self.c
        self.c = res
        return res