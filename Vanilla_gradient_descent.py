#!/usr/bin/python

import numpy, math
learning_rate=0.1
test_data = [[[0,0],0],[[0,1],1]]
#grad should be (0,-0.25)
#w should be (0,0.025)
#for one iteration with the test data


#Testing function
def theta(x,w):
    x.insert(0,1)
    x = numpy.array(x)
    s = numpy.dot(w,x)
    return (math.e**s)/(1+math.e**s)

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

    for i in range(1000):
        #Calcluate grad f
        grad = zero
        for x in data:
            x_vec = numpy.array(x[0])
            coeff = x[1]/(1+math.e**(x[1]*numpy.dot(w,x_vec)))
            grad = grad + coeff*x_vec
        grad = (-(1.0/len(data)))*grad
        w = w - learning_rate*grad
        
    return w
