__author___ = 'Lukas Koerber'

from numpy import *
import matplotlib.pyplot as plt



"""

Zunaechst werden aus den Parametern t die Koordinaten bestimmt.

x = r(t) * cos ( phi(t) )
y = r(t) * sin ( phi(t) )

"""

t = arange(0.,3.0,0.03)                                                 # erzeugt Parametermenge
x = (0.5 ** t) * cos(2 * pi * t)                                        # x-Koordinate = r * cos ( phi )
y = (0.5 ** t) * sin(2 * pi * t)                                        # y-Koordinate = r * sin ( phi )


fig = plt.figure()
fig.set_size_inches(8.27, 11.69)
ax = fig.add_subplot(111, aspect=1.0)
ax.plot(x,y)


def onclick(event):
    event.canvas.figure.clear()                                          # loesche Daten im Canvas
    event.canvas.figure.gca().plot(x,y)                                  # plot urpruengliche Spirale
    event.canvas.figure.gca().plot(x-event.xdata,y-event.ydata)          # plot verschobene Spirale
    event.canvas.draw()                                                  # erzeuge erneutes Canvas

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()