#!/usr/bin/python


def dot_prod(a,b):
    '''This class takes two vectors in form [a1,a2,a3...an] and returns their dot product.'''
    result = 0
    for i in range(len(a)):
        result+=a[i]*b[i]
    return result


def add_vec(a,b):
    '''This adds the two vectors a,b in the form [a1,a2,a3,....an]'''
    result=[]
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result




def PLA(data, w0=[]):
    ''' This is a class that implements the PLA learning algorithm.
    data is in the form [[[x11,x12,x13,....x1n],y1],.....[[xN1,xN2,...xNn],yN]]
    w0 is the initial weight vector which is optional.
    '''
        
    #transform data to add x0 coordinate for final weight vector
    for x in data:
        x[0].insert(0,1)
    
    #initialising weight vector if zero
    if w0 == []:
        for i in range(len(data[0][0])):
            w0.append(0)
        
    #PLA while cycle
    errorflag = True
    while errorflag:
        errorflag=False
        for x in data:
            calc = dot_prod(w0,x[0])
            if (calc >= 0 and x[1]==-1) or (calc<0 and x[1]==1):
                w0 = add_vec(w0,x[0])
                errorflag=True
                break
    return w0


