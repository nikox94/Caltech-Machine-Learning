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
w = [1,1]
i=0
while v>=10**(-14):
    w = subtract_vecs(w,rmult(eta,grad_f(w[0],w[1])))
    v = f(w[0],w[1])
    i+=1
