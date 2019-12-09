# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:02:26 2019

@author: admin
"""

import itertools
from GF2 import one
import vec

#class Vec:
#    def __init__(self, labels, function):
#        self.D = labels
#        self.f = function


# v = Vec({'A', 'B', 'C'}, {'A': 1})
'''
for d in v.D:
    if d in v.f:
        print(v.f[d])
'''


def zero_vec(D):
    return Vec(D, {d: 0 for d in D})
# we can also return (D,{}) to preserve sparsity


def setitem(v, d, val): v.f[d] = val


def getitem(v, d): return v.f[d] if d in v.f else 0


def scalar_mul(v, alpha): return Vec(
    v.D,
    {d: alpha*getitem(v, d) for d in v.D}
)

# writing alpha*v.f[d] is giving error as for loop goes and uses dict values of
# all domain elements
# we can also write d: alpha*value for d, value in v.f.items() which preserves
# sparsity
# print(scalar_mul(v, 2).f)


def add(u, v):
    if u.D == v.D:
        return Vec(u.D, {d: getitem(u, d) + getitem(v, d) for d in u.D})


def neg(v): return scalar_mul(v, -1)
# return Vec(v.D,{d:-getitem(v,d) for d in v.D})
# return vec(v.D, {key: -value for key,value in v.f.items()})


'''
s = Vec({(i, j) for i in range(5) for j in range(5)},
{(0, 0): one, (0, 1): one, (0, 2): one, (0, 3): one, (0, 4): 0,
(1, 0): one, (1, 1): one, (1, 2): one, (1, 3): 0, (1, 4): one,
(2, 0): one, (2, 1):one, (2, 2): one, (2, 3): 0, (2, 4): one,
(3, 0) :0, (3, 1) :0, (3, 2): 0, (3, 3): one, (3, 4): one,
(4, 0) :one, (4, 1): one, (4, 2): 0, (4, 3): one, (4, 4): one})
'''
# s = Vec({(i, j) for i in range(2) for j in range(2)},
# {(0, 0): one, (0, 1): one, (1,0):0,(1,1):0})
# v = zero_vec({(i, j) for i in range(2) for j in range(2)})
s = Vec({(i, j) for i in range(5) for j in range(5)},
       {(0, 0): one, (0, 1): one, (0, 2): 0, (0, 3): 0, (0, 4): 0,
(1, 0): one, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
(2, 0): 0, (2, 1):0, (2, 2): 0, (2, 3): 0, (2, 4): 0,
(3, 0) :0, (3, 1) :0, (3, 2): 0, (3, 3): 0, (3, 4): one,
(4, 0) :0, (4, 1): 0, (4, 2): 0, (4, 3): one, (4, 4): one})
v = zero_vec({(i, j) for i in range(5) for j in range(5)})
L = []


def create_gf2_vec(i, j):
    u = zero_vec(v.D)
    setitem(u, (i, j), one)
    if (i-1, j) in u.D:
        setitem(u, (i-1, j), one)
    if (i+1, j) in u.D:
        setitem(u, (i+1, j), one)
    if (i, j+1) in u.D:
        setitem(u, (i, j+1), one)
    if (i, j-1) in u.D:
        setitem(u, (i, j-1), one)
    return u


for i in range(5):
    for j in range(5):
        L.append(create_gf2_vec(i, j))

def find_solution(L,s):
    for i in range(6):
        vect_combi_list = list(itertools.combinations(L,i))
        for t in vect_combi_list:
            temp_vect = zero_vec({(i, j) for i in range(5) for j in range(5)})
            for j in t:
                temp_vect = add(temp_vect,j)
                if temp_vect.f == s.f:
                    print('solution exists')
                    return t
    print('no solution')


# sol = find_solution(L,s)
def list2vec(L):
    """Given a list L of field elements, return a Vec with domain
    {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k: L[k] for k in range(len(L))})


def dot(u, v):
    assert u.D == v.D
    return sum(list(getitem(u, d) * getitem(v, d) for d in u.D))


u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
u2 = Vec({'a', 'b'}, {'b': 2, 'a': 1})
v1 = Vec({'p', 'q', 'r', 's'}, {'p': 2, 's': 3, 'q': -1, 'r': 0})
v2 = Vec({'p', 'q', 'r', 's'}, {'p': -2, 'r': 5})
assert dot(u1, u2) == 5
assert dot(v1, v2) == -4
assert u1 * u2 == 5


def list_dot(u, v): return dot(list2vec(u), list2vec(v))


assert list_dot([1, 2, 3], [1, 2, 3]) == 14


def dot_product_list(needle, haystack):
    s = len(needle)
    return [dot(needle, haystack[i:i+s]) for i in range(len(haystack)-s)]

def triangular_solve_n(rowlist, b):
    D = rowlist[0].D
    x_vector = zero_vec(D)
    n = len(D)
    assert D == set(range(n))
    for i in reversed(range(n)):
        x_vector[i] = (b[i] - rowlist[i]*x)/rowlist[i][i]
    return x




