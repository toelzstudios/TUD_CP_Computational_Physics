__author__ = 'Lukas'



from numpy import *
import matplotlib.pyplot as plt


def phase_std(q_0, p_0, K, N = 1000):
    q, p = zeros(1000), zeros(1000)
    q[0], p[0] = q_0, p_0
    for n in range(1,N-1):
        q[n] = (q[n-1] + p[n-1])%(2*pi)
        p[n] = (p[n-1] + K * sin(q[n])+ pi) % (2*pi) - pi
    return [q, p]


varK = 2.6

fig = plt.figure()
fig.set_size_inches(16.27, 22.69)
ax = fig.add_subplot(111, aspect=1.0)
ax.set_xlim([0,2*pi])
ax.set_ylim([-pi,pi])



def onclick(event):
    print ("q_0: {} , p_0: {}, K: {}".format (event.xdata, event.ydata, varK))
    x = phase_std(event.xdata,event.ydata,varK)[0]
    y = phase_std(event.xdata,event.ydata,varK)[1]
    event.canvas.figure.gca().plot(x, y, '.')
    event.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

