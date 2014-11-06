#!/usr/bin/python

from Vanilla_gradient_descent import *
from Create_data_set_in_R2 import *

learning_rate=0.01

def GD(data):
    '''This performs the said algorithm with data being in the form
    [ [ [xN1, xN2, ....],y1], ....]
    '''

    #transform data to add x0 coordinate for final weight vector
    for x in data:
        x[0].insert(0,1)

    #initialising weight vector if zero
    w = []
    for i in range(len(data[0][0])):
        w.append(0)

    w = numpy.array(w)
    zero = numpy.array(w)
    old_w = numpy.array([1,100,100])
    
    while numpy.linalg.norm(w-old_w)>=0.005:
        #Calcluate grad f
        grad = zero
        for x in data:
            x_vec = numpy.array(x[0])
            coeff = x[1]/(1+math.e**(x[1]*numpy.dot(w,x_vec)))
            grad = grad + coeff*x_vec
        grad = (-(1.0/len(data)))*grad
        old_w = w
        w = w - learning_rate*grad
        
    return w

g_error=[]

for i in range(100):
    A = gen_line_classification_algorithm_data()
    data = A[2]
    x1 = A[0]
    x2 = A[1]

    eout_data = gen_eout_sample(x1,x2)
    
    w = GD(data)
    print 'baby'
    error = []
    for e in eout_data:
        error.append(theta(e[0],w)-e[1])
    avg = 0
    for e in error:
        avg+=e
    avg = avg/len(error)
    g_error.append(avg)

print g_error
for e in g_error:
    avg+=e
avg = avg/len(g_error)
print avg
    
