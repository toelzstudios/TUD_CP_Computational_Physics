__author__ = 'Lukas Koerber'

"""The purpose of this programm is to compute the derivative of a function using three different numerical methods and
thereby comparing the deviation to the analytical solution. In his case the given function is 'arctan(x^2)' whereas the
point of interest is x_0 = 1/3"""

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

"""Since some builtin math operations such as '*' and '**' do not support element wise computation I used numpy
 functions (i.e. divide(), square()) instead."""


# Given function and its first derivative.

def f(x):
    return arctan(square(x))

def df(x):
    return divide(multiply(2.,x),square(square(x))+1)


# Numerical methods

def deriv(func, x, h, method="extrapolate"):
    """deriv(func, x, h[, method]) returns the first derivative of 'func' at 'x' using a step size of 'h'. Normally,
    the computation method is "extrapolate", but can also be set to "forward" or "central" using the 'method'
    parameter."""
    if method == "extrapolate":
        return divide(multiply(8,func(x+divide(h,4))-func(x-divide(h,4))) - \
                    (func(x+divide(h,2))-func(x-divide(h,2))), multiply(3,h))
    elif method == "forward":
        return divide(func(x+h) - func(x),h)
    elif method == "central":
        return divide(func(x+divide(h,2))-func(x-divide(h,2)),h)

def error(x,y):
    return absolute(x - y)


pows = []

dh = 1
for i in arange(-10.,1.,dh):
    pows.append(10.**i)

x2 = 1./3 * ones(len(pows))

fig = plt.subplot(111, xscale="log", yscale="log")
for s in ["forward", "central", "extrapolate"]:
    fig.plot(pows, error(deriv(f, x2, pows, s),df(x2)))

fig.plot(pows, power(pows,1), c='b', ls='--')
fig.plot(pows, power(pows,2), c='g', ls='--')
fig.plot(pows, power(pows,4), c='r', ls='--')

"""The extrapolation method scales with h**4. Please see attachment 2.1.a) for confirmation."""


blue_patch = mpatches.Patch(color='b')
red_patch = mpatches.Patch(color='r')
green_patch = mpatches.Patch(color='g')
black_dotted = mlines.Line2D([],[],c="k",ls="--")


plt.legend((blue_patch, green_patch, red_patch, black_dotted),(r'Vor\"artsdifferenz',"Zentraldifferenz","Extrapoliert",
                                                               "Skalierungsverhalten"),loc=4)

plt.show()



"""Es zeigt sich bei bla bla bla.."""


