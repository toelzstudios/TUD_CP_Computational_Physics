from __future__ import division
__author__ = 'Lukas'

"""
Exercise 3.1:

Description here....
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

blue_patch = mpatches.Patch(color='b')
red_patch = mpatches.Patch(color='r')
green_patch = mpatches.Patch(color='g')
black_dotted = mlines.Line2D([], [], c="k", ls="--")


c = []

int_a = - 1./4
int_b = 0.177245385090
int_c = np.pi/3

x1 = -np.pi/2
x2 = np.pi/3


def func_a(x):
    return np.sin(np.multiply(2,x))


def func_b(x):
    return np.exp(-np.multiply(100,np.square(x)))


def func_c(x):
    return np.multiply(0.5,1.0+np.sign(x))



def integ(func, start, end, n, method="simpson"):
    h = float(end-start)/n
    x = start + h/2
    intsum = 0.0
    if method == "simpson":
        return 0
    elif method == "center":
        while x < end:
            intsum += h*func(x)
            x += h
        return intsum
    elif method == "trapeze":
        return 0


def error(x,y):
    """
    Returns the relative error of x to y.
    """
    return np.absolute(np.divide(x - y, y))

def mcolor(method):
    """
    Return a color specific for a certain method.
    """
    if method == "simpson":
        return "red"
    elif method == "center":
        return "blue"
    elif method == "trapeze":
        return "green"


def mscale(method):
    """
    Return the power n such that the error of a method is proportional to h**n.
    """
    if method == "simpson":
        return ######
    elif method == "center":
        return ######
    if method == "trapeze":
        return ######
"""

for m in ["simpson", "center", "trapeze"]:
    fig.plot(myh, error(integ(func_a, start, end, method = m), int_a), color=mcolor(m))
    fig.plot(myh,
             np.multiply(np.power(myh,mscale(m)),
                         np.absolute(df(x0)-deriv(f, x0, 1., m))),
             c=mcolor(m), ls='--')

"""
a = []
b = []
for n in np.linspace(1, 4, 100):
    a.append((x2-x1)/(10**n))
    # b.append(np.absolute((integ(func_b, x1, x2, 10**n, method="center") - int_b)/int_b))
    c.append(np.absolute((integ(func_a, x1, x2, 10**n, method="center") - int_a)/int_a))

print integ(func_a, x1, x2, 1000, method="center")
x = np.linspace(x1, x2, 1000)
fig = plt.subplot(111, xscale="log", yscale="log")
fig.plot(a, c)
# fig.plot(a, b)
plt.show()