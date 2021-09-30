def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    components = []
    for xi, yi in zip(x, y):
        components.add(abs(xi - yi))
    return sum(components)

def jaccard_dist(x, y):
    # jaccard = size of intersection / size of union
    intersection = list(set(x).intersection(y))
    intersectionCardinality = len(intersection)
    unionCardinality = (len(x) + len(y)) - intersectionCardinality
    if unionCardinality == 0:
        return 0
    return float(intersectionCardinality) / unionCardinality

def cosine_sim(x, y):
    a = sum(xi * yi for xi, yi in zip(x, y))
    b = sum(xi**2 for xi in x)**(1/2)
    c = sum(yi**2 for yi in y)**(1/2)
    return a/(x*y)

# Feel free to add more
