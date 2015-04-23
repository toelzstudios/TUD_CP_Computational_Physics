"""
Exercise 1.1:

The task is to illustrate the phase space path of a kicked rotor with different
initial conditions and thereby examining the characteristic phase regions of a
chaotic system.
If you wish to set initial conditions, use mouse clicks to spawn a path in the
plot figure.
""" 

__author__ = 'Lukas Koerber'

print __doc__
    
import numpy as np
import matplotlib.pyplot as plt

varK = 2.6

def phase_std(q_0, p_0, k, n = 1000):
    """
    Return the phase space path as two arrays of a kicked rotor for initial
    canonical coordinates q_0, p_0 and a kick strength of K using n (default is
    1000) iterations.
    """
    q, p = np.zeros(1000), np.zeros(1000)
    q[0], p[0] = q_0, p_0
    for i in range(1,n-1):
        q[i] = (q[i-1] + p[i-1])%(2*np.pi)
        p[i] = (p[i-1] + k * np.sin(q[i])+ np.pi) % (2*np.pi) - np.pi
    return [q, p]

# In phase_std the q and p arrays are created right at the beginning to take
# advantage of the array arithmetic of numpy and spare using the .append()
# method. Having them in memory from the start on should not effect runtime.

def click(event):
    """
    If toolbar mode is set to normal plot phase_std using the xdata and ydata
     of the mouse click event as initial conditions.
    """
    if plt.get_current_fig_manager().toolbar.mode == '':
        x = phase_std(event.xdata,event.ydata,varK)[0]
        y = phase_std(event.xdata,event.ydata,varK)[1]
        event.canvas.figure.gca().plot(x, y, '.')
        event.canvas.draw()
        # The draw() method is similiar to show() but it actually enables
        # editing the plot while it is already shown.

fig = plt.figure()
fig.set_size_inches(16.27, 22.69)
ax = fig.add_subplot(111, aspect=1.0)
ax.set_xlim([0,2*np.pi])
ax.set_ylim([-np.pi,np.pi])


listener = fig.canvas.mpl_connect('button_press_event', click)
# This will register the canvas for the mouse click event. It is important to
# note that the figure will automatically be unregistered if it is closed, so
# there is no need to do it manually.

plt.show()

# Observations:
#
# While zooming in at the peripheral areas the fractal nature of the phase
# space of a chaotic system becomes very obvious as while zooming more and
# more small 'islands' of regular behavior become visible. As one zooms in
# at these islands again smaller islands appear at their borders.
