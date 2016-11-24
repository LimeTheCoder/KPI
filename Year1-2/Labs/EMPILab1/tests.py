import numpy as np

# Function to compute stirling numbers
def stirling(n,k):
    if n == k:
        return 1

    if k == 0 or n == 0:
        return 0

    return stirling(n - 1, k - 1) + k * stirling(n - 1, k)

# Theoretical probabilities for partiotion criteria
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


# Theoretical probabilities for coupon criteria
def coupon_theor(d, r=0, t=0, compute_for_t=False):
    if compute_for_t:
        p = 1.0 - np.math.factorial(d) / float(d**(t - 1)) * stirling(t-1, d)
    else:
        p = np.math.factorial(d) / float(d**r) * stirling(r-1, d-1)

    return p

# Practic frequences for coupon criteria
def coupon_practic(gen, t, d, n):
    count = np.zeros(t - d + 1)
    for i in range(n):
        occurs = np.zeros(d)
        q, r = 0, 0

        while True:
            r += 1
            if r >= t:
                break

            num = gen.next()
            if occurs[num] != 0:
                continue

            occurs[num] = 1
            q += 1

            if q == d:
                break

        if r >= t:
            count[t - d] += 1
        else:
            count[r - d] += 1

    return count
