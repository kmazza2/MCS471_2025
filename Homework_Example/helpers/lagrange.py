from math import prod

def _L(k, x, data):
    numerator_factors = [
        (x - point[0])
        for i, point in enumerate(data)
        if i != k
    ]
    denominator_factors = [
        (data[k][0] - point[0])
        for i, point in enumerate(data)
        if i != k
    ]
    return prod(numerator_factors) / prod(denominator_factors)

def lagrange(data, x):
    terms = [
        (point[1] * _L(i, x, data))
        for i, point in enumerate(data)
    ]
    return sum(terms)
