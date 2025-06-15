from helpers.lagrange import lagrange

data_a = (
        (1970, 3707475887),
        (1990, 5281653820)
)
data_b = (
        (1960, 3039585530),
        (1970, 3707475887),
        (1990, 5281653820)
)
data_c = (
        (1960, 3039585530),
        (1970, 3707475887),
        (1990, 5281653820),
        (2000, 6079603571)
)
results = [
        lagrange(data, 1980)
        for data in (data_a, data_b, data_c)
]
compare = [item - 4452584592 for item in results]

print(results[0])
print(results[1])
print(results[2])
print(compare)
