from __future__ import division
__author__ = 'Basti'


import numpy as np
import matplotlib.pyplot as plt


"""
Umrechnung con Polar- in kartesische Koordinaten:
    x = r * cos(phi)
    y = r * sin(phi)
"""

t = np.arange(0.0, 5.0, 0.01)


def build_plot(x_0, y_0):
    x_new = 0.5**t * np.cos(2*np.pi*t) + x_0
    y_new = 0.5**t * np.sin(2*np.pi*t) + y_0
    return x_new, y_new


def click_event(fappening):
    x, y = build_plot(fappening.xdata, fappening.ydata)
    plt.plot(x, y)
    plt.draw()

fig1 = plt.figure(0)
plt.subplot(111, aspect=1.0)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title('Spirale')
plt.xlabel('x')
plt.ylabel('y')

plt.connect('button_press_event', click_event)
plt.show()