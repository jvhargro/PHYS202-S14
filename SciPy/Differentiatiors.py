

import numpy as np
import matplotlib.pyplot as plt

def TwoPtForwardDiff(x,y):
    """Takes the forward derivitave of an array of x and y values, then
    corrects for the endpoints by taking a backwards derivative"""
    dydx = np.zeros(y.shape,float) 
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def TwoPtCenteredDiff(x,y):
    """the slope is calculated at the center of each x value except for the endpoints which
    are handled separately"""
    dydx1 = np.zeros(y.shape,float)

    dydx1[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx1[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx1[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])

    return dydx1

def FourPtCenteredDiff(x,y):
    """ The slope is calculated from the center using the two points to the right and left,
    the two points on either end left over are calculated using forward and backwards
    derivatives"""
    
    dydx2 = np.zeros(y.shape,float)
    h = x[1] - x[0]
    dydx2[2:-2] = (y[0:-4]-8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*h)
    
    dydx2[0:2] = np.diff(y[0:2])/np.diff(x[0:2])
    dydx2[-2:-1] = (y[-2:-1] - y[-1:])/(x[-2:-1] - x[-1:])

    return dydx2
    