import random
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from lsh import *

random.seed(2)

def init_space(n_points=20, dim=2):
    space = []
    for i in range(n_points):
        v = [random.gauss(0, 1) for z in range(dim)] 
        space.append(v)

    return space

def closest_point(q, space):
    scores = cosine_similarity([space[q]], space)
    scores[0][q] = 0
    return scores, np.argmax(scores)

space = init_space(n_points=20)
scores, closest = closest_point(0, space)
tables, planes = lsh(space)

print(scores, closest)
print(predict(0, space, tables, planes))





