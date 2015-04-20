from __future__ import division
__author__ = 'Sebastian Schmidt'

from numpy import *
import matplotlib.pyplot as plt


class PSS(object):                                 # for Phase Space State

    """
    This class contains information about the Phase State of the rotor. Also it
    includes a method to generate the next state from the latest state
    information using the given formulas.
    """

    def __init__(self, theta_0, p_0, k=1.0):
        self.theta = [theta_0 % (2*pi)]            # list of theta values
        self.p = [(p_0 + pi) % (2*pi) - pi]        # list of p values
        self.K = k

    def evolve(self):
        self.theta.append((self.theta[-1] + self.p[-1]) % (2 * pi))
        self.p.append((self.p[-1] + self.K * sin(self.theta[-1])+pi)%(2*pi)-pi)


def onclick(event):

    """
    This function creates a PSS class, initializes it with the xdata- and
    ydata-values of the lift-click-event and plots the next 1000 Phase Space
    States using the .evolve function. It also filters out wrong user input and
    handles the case of zooming into the picture.
    """

    """
    Check first, if the user left-clicked on the plotting area and then if he
    is not in zooming mode
    """
    if event.xdata != None and event.ydata != None and event.button == 1:
        if plt.get_current_fig_manager().toolbar.mode == '':
            start = PSS(event.xdata, event.ydata)  # initializing PSS class
            for i in range(1, 1000):               # with clicked on coords,
                start.evolve()                     # creating the next 1000
            plt.plot(start.theta, start.p, '.')    # Phase Space States and
            plt.draw()                             # plotting them
    else:
        print "Please click left on the Plotting Area"


plt.subplot(111, aspect=1.0)                       # fixed quadratic plotting
plt.xlim(0, 2*pi)                                  # area
plt.ylim(-pi, pi)
plt.title('Kicked Rotor')
plt.xlabel('Theta')
plt.ylabel('p')

plt.connect('button_press_event', onclick)         # calling function onclick
plt.show()                                         # by clicking on the window


"""
Textgelaber
"""
