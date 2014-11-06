#!/usr/bin/python

from math import e

def f(u,v):
    result = u*e**v-2*v*e**(-u)
    return result**2

def grad_f(u,v):
    return [2*(u*e**v-2*v*e**(-u))*(e**v+2*v*e**(-u)),2*(u*e**v-2*v*e**(-u))*(u*e**v-2*e**(-u))]

def rmult(const,a):
    result = []
    for i in range(len(a)):
        result.append(const*a[i])
    return result

def subtract_vecs(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i]-b[i])
    return result

v = f(1,1)
eta = 0.1
x=1
y=1
for i in range(15):
    x = x - eta*(grad_f(x,y)[0])
    y = y - eta*(grad_f(x,y)[1])
    v = f(x,y)
print v
#Coordinate descent sucks. Only v~10^-1 for 15 iterations vs 10^-14 for 10 iterations of gradient descent
