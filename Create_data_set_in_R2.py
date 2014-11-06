#!/usr/bin/python

import random

def gen_line_classification_algorithm_data():
    #Pick two random points and "draw a line"
    x1 = [random.uniform(-1,1), random.uniform(-1,1)]
    x2 = [random.uniform(-1,1), random.uniform(-1,1)]
    m = (x1[1]-x2[1])/(x1[0]-x2[0])
    def prava(x):
        return m*x+x1[1]-m*x1[0]

    #generate 100 random points
    A = []
    for i in range(100):
        x = [random.uniform(-1,1), random.uniform(-1,1)]
        A.append(x)

    #evaluate the classification function on them
    for i in range(len(A)):
        if A[i][1]<prava(A[i][0]):
            A[i] = [A[i],-1]
        else:
            A[i] = [A[i],1]
    return (x1,x2,A)


def gen_eout_sample(x1,x2):
    #"Draw line"
    m = (x1[1]-x2[1])/(x1[0]-x2[0])
    def prava(x):
        return m*x+x1[1]-m*x1[0]
    
    #generate 100 random points
    A = []
    for i in range(100):
        x = [random.uniform(-1,1), random.uniform(-1,1)]
        A.append(x)

    #evaluate the classification function on them
    for i in range(len(A)):
        if A[i][1]<prava(A[i][0]):
            A[i] = [A[i],-1]
        else:
            A[i] = [A[i],1]
    return A