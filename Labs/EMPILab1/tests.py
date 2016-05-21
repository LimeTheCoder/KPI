import numpy as np


def stirling(n,k):

    if n == k:
        return 1

    if k == 0 or n == 0:
        return 0

    return stirling(n - 1, k - 1) + k * stirling(n - 1, k)


def get_partition_theor(d, k):
    prob_lst = []
    denominator = d ** k
    for r in range(1, k + 1):
        s = 1

        for i in range(r):
            s *= (d - i)

        p = float(s) / denominator * stirling(k, r)
        prob_lst.append(p)

    return np.array(prob_lst)