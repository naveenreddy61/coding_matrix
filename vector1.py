# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:16:32 2019

@author: admin
"""

from plotting import plot
L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1],
     [2.75, 1], [3, 1], [3.25, 1]]
# plot(L,4,2)
# 2d vector addition


def add2(u, v):
    return [u[0]+v[0], u[1]+v[1]]


# plot([add2([1,2],v) for v in L],4,2)
# nd vector addition
def addn(u, v):
    return [a+b for (a, b) in zip(u, v)]


# plot([addn([1,2],v) for v in L],4,2)

# scalar multiplication of nd vector with alpha


def scalar_vector_mul(alpha, v):
    return [alpha*v[i] for i in range(len(v))]


# plot([scalar_vector_mul(0.5,v) for v in L],4,2)

# line segment through origin
v = [3, 2]
# plot([scalar_vector_mul(i/10,v) for i in range(11)],4,2)
# plot([scalar_vector_mul(i/100,v) for i in range(101)],4,2)
# plot([scalar_vector_mul(i/10,v) for i in range(11) for v in L],4,2)
# plot([1,2],4)

# plotting any line segment from (0.5,1) to (3.5,3)
plot([add2(scalar_vector_mul(i/100, [3, 2]), [0.5, 1])
     for i in range(101)], 4)
