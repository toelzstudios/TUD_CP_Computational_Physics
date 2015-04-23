"""
Author: Lukas Koerber,
Exercise 2.1:

The purpose of this programm is to compute the derivative of a function using
three different numerical methods and comparing the deviation to the analytical
solution. In his case the given function is 'arctan(x^2)' whereas the point of
interest is x_0 = 1/3.
"""

__author__ = 'Lukas Koerber'

print __doc__

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# The patches and lines packages are later use for the plot legend. Also, in
# this programm I mainly use numpy functions (i.e. divide() and square())
# instead of the basic * and ** when computing arrays element wise because the
# latter operator sometimes cause problems in that case.

myh = np.power(10, np.linspace(-10, 0, 1000))
x0 = 1./3

blue_patch = mpatches.Patch(color='b')
red_patch = mpatches.Patch(color='r')
green_patch = mpatches.Patch(color='g')
black_dotted = mlines.Line2D([], [], c="k", ls="--")


def f(x):
    """
    Returns the value of the function given for this exercise.
    """
    return np.arctan(np.square(x))


def df(x):
    """
    Returns the analytical derivative of f at x.
    """
    return np.divide(np.multiply(2.,x),np.square(np.square(x))+1)


def deriv(func, x, h, method="extrapolate"):
    """
    Returns the first derivative of 'func' at 'x' using a step size of 'h'.
    Normally, the computation method is "extrapolate", but can also be set to
    "forward" or "central" using the 'method' parameter.
    """
    if method == "extrapolate":
        return np.divide(np.multiply(8,func(x+np.divide(h,4)) - \
                func(x-np.divide(h,4))) - (func(x+np.divide(h,2)) - \
                func(x-np.divide(h,2))), np.multiply(3,h))
    elif method == "forward":
        return np.divide(func(x+h) - func(x), h)
    elif method == "central":
        return np.divide(func(x+np.divide(h,2))-func(x-np.divide(h,2)), h)

def error(x,y):
    """
    Returns the relative error of x to y.
    """
    return np.absolute(np.divide(x - y, y))


def mcolor(method):
    """
    Return a color specific for a certain method.
    """
    if method == "extrapolate":
        return "red"
    elif method == "forward":
        return "blue"
    elif method == "central":
        return "green"


def mscale(method):
    """
    Return the power n such that the error of a method is proportional to h**n.
    """
    if method == "central":
        return 2
    elif method == "forward":
        return 1
    if method == "extrapolate":
        return 4
        # This was not given but I proved it via Taylor expansion using
        # Wolfram Alpha. But one can also just try fitting.

fig = plt.subplot(111, xscale="log", yscale="log")
for m in ["forward", "central", "extrapolate"]:
    fig.plot(myh, error(deriv(f, x0, myh, m),df(x0)), color=mcolor(m))
    fig.plot(myh,
             np.multiply(np.power(myh,mscale(m)),
                         np.absolute(df(x0)-deriv(f, x0, 1., m))),
             c=mcolor(m), ls='--')

plt.legend(
    (blue_patch, green_patch, red_patch, black_dotted),
    ('Voraertsdifferenz',"Zentraldifferenz","Extrapoliert",
            "Skalierungsverhalten"),
    loc=4)

plt.show()

# Observations:
#
# Of course 10e-10 does not bring the best solutions for all three methods,
# because at a certain degree of finesse the numeric error error gets bigger
# and bigger and the error curves begin to rise again after a certain minimum.
#
# The forward method appears to be the worst method with a optimal h of around
# 10e-9 and a minimal error of 10e-8. The forward method is slightly better
# with a optimal h of 10e-6 and a minimal error of 10e-12. By far the best
# solution is given py the extrapolation method with a optimal h of 0.0019 and
# an error of just around 10e-14.



