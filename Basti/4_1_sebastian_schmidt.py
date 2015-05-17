"""
Aufgabe 3.1

Dieses Programm dient dem Kennenlernen der Loesungsmethode 'odeint' zur
Loesung gewoehnlicher Differentialgleichungen 1. Ordnung aus dem python-
Paket scipy. Hier wird es beispielhaft demonstriert an einer gegebenen
Hamilton-Funktion:

H(x, p) = 0.5*p**2 + x**4 - x**2 + x*(A + B*sin(omega * t)

mit den gegebenen Konstanten A = B = 0.1 und omega = 1.
Mittels der kanonischen Gleichungen kann man aus der Funktion ein System
zweier Differentialgleichungen 1. Grades fuer x und p machen
(s. Funktion odesys()) und die so ermittelten diskreten Werte fuer x und
p im Phasenraum gegneinander plotten. Zusaetzlich wir eine
Stroboskopische Darstellung erzeugt, welche das System nur zu ganz
bestimmtenn Zeiten t_i zeigt, naemlich immer nach einer vollen Periode,
des Sinusses im zeitabhaengigen Potential.

Das Plotfenster dient dem Nutzer ausserdem zur Festlegung der Anfangs-
bedingungen fuer das System. Dazu wird mit der linken Maustaste in eines
der beiden Fenster geklickt und die so ausgewaehlten Koordinaten als
Ausgangspunkt einer neuen Trajektorie festgelegt.  
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def odesys(phi, t, a, b, om):
    """
    Rechte Seite des DGL-Systems welches die kanonischen Gleichungen aus
    der gegebenen Hamilton-Funktion fuer den Phasenraumvektor
    phi = [x, p] liefern.
    a, b und om sind die entsprechenden Parameter der Hamilton-Funktion;
    t die Zeit.
    """
    return np.array([phi[1], -4*phi[0]**3 + 2*phi[0] -
          (a + b*np.sin(om*t))])


def onclick(event):
    """
    Diese Funktion wird aufgerufen, wenn auf das geoeffnete 
    figure-Fenster geklickt wird. Sie ueberprueft zunaechst, ob in
    einen der beiden Achsenbereiche geklickt wurde und dann ob der
    Nutzer im normalen Modus ist (und nicht z.B. im Zoom-Modus). Wenn
    beide Abfragen zutreffen plottet sie die mithilfe der 'odeint'-
    Funktion errechneten Werte fuer x und p der gegebenen Hamilton-
    Funktion mit den per Mausklick ausgewaehlten Anfangsbedingungen.
    Falls nicht in einen Achsenbereich geklickt wurde, wird ein Hinweis
    zur Benutzerfuehrung ausgegeben. 
    """	
    if event.button == 1 and event.inaxes:
        if fig.canvas.toolbar.mode == '':
            phi_0 = np.array([event.xdata, event.ydata])
            phi_t = odeint(odesys, phi_0, times, args=(A, B, omega))
            x_t = phi_t[:, 0]
            p_t = phi_t[:, 1]
            ax_p.plot(x_t, p_t, '.', ms=3)
            ax_s.plot(x_t[::steps], p_t[::steps], '.', ms=3)
            plt.draw()
    else:
        print "Bitte klicken Sie links in eins der beiden Plotfenster."


# Parameter der Hamilton-Funktion als globale Variablen
A = 0.1
B = 0.1
omega = 1

# Anzahl der Perioden des Sinus im Potential ('rotations') sowie Anzahl
# der Zeitpunkte t_j pro Periode ('steps')
periods = 200
steps = 20

# Anlegen des Array fuer die Zeiten, zu denen das System untersucht 
# werden soll 
times = np.linspace(0, 2 * np.pi * periods, steps * periods)


# Anlegen von x- und p-Arrays, welche mittels np.meshgrid() in zweidimensionale
# Gitter ueberfuehrt werden, damit nachher mit plt.contour() die Niveaulinien
# 'energies' der Hamilton-Funktion 'H' in die Plotfenster eingezeichnet werden
# koennen
x = np.linspace(-2.0, 2.0, 200)
p = np.linspace(-5.0, 5.0, 200)
xm, pm = np.meshgrid(x, p)
H = 0.5*pm**2 + xm**4 - xm**2 + A*xm
energies = np.array([-0.3, -0.2, -0.075, 0.0026, 0.18, 0.3, 0.5, 0.75])


# Anlegen der Figure und unterteilen dieser in die zwei Achsenbereiche ax_p
# und ax_s (fuer stroboskopisch). Diese werden entsprechend gelabelt und
# gleichermassen auf einen bereich beschraenkt, der die wichtigsten Infos des
# Phasenraums enthaelt
fig = plt.figure(figsize=(20, 10))
fig.suptitle('Phasenraum', fontsize=25)

ax_p = fig.add_subplot(121)
ax_p.set_title('normale Darstellung')
ax_p.set_xlim(-1.5, 1.5)
ax_p.set_ylim(-1.5, 1.5)
ax_p.set_xlabel('$x$')
ax_p.set_ylabel('$p$')

# Energielinien einzeichnen
cont1 = ax_p.contour(xm, pm, H, levels=energies, colors='k')
ax_p.clabel(cont1, inline=1, fontsize=10)

# gleiche Vorgehensweise wie bei ax_p
ax_s = fig.add_subplot(122)
ax_s.set_title('Stroboskopische Darstellung')
ax_s.set_xlim(-1.5, 1.5)
ax_s.set_ylim(-1.5, 1.5)
ax_s.set_xlabel('$x$')
ax_s.set_ylabel('$p$')

cont2 = ax_s.contour(xm, pm, H, levels=energies, colors='k')
ax_s.clabel(cont2, inline=1, fontsize=10)


# Verknuepfen des Klick-Events mit der Funktion onclick()
fig.canvas.mpl_connect('button_press_event', onclick)

# Hauptprogramm, docstring zur Benutzerfuehrung, Erzeugen der figure
print __doc__
plt.show()


"""
Aufgabe 4.1

a) Fuer B = 0 ist das Potential ein zeitunabhaengiges asymmetrisches Doppel-
muldenpotential. Im Phasenraum ist daher zu erwarten, dass man geschlossene
Bahnen in beiden Mulden vorfindet. Da das Potential sowohl fuer -x als auch x
gegen Unendlich geht wird es aufgrund von Reflexion des Teilchens im
Unendlichen allerdings ausschliesslich geschlossene Bahnen geben, welche dann
auch ueber die mittlere Potentialschwelle bei x = 0 hinaus gehen. Diese drei
Phasenraumbereiche (geschlossene Bahnen in den beiden Mulden + geschlossene
globale Bahnen) werden durch eine Separatrix getrennt, welche durch die
Niveaulinie H(x,p) ~ 0.0027 bestimmt wird.

b) Die in a) beschriebenen Phasenraumbahnen entsprechen im Ortsraum
periodischen Oszillationen. Man kann es sich anschaulich vorstellen als eine
Kugel, welche in dem Potential hin- und herrollt: es gibt kleine Oszillationen
in den Mulden, wenn der Anfangswert von p nicht zu gross gewaehlt wird, welche
den geschlossenen Bahnen im Phasenraum entsprechen. Die globalen geschlossenen
Bahnen entsprechen dabei Oszillationen, bei denen die Kugel auch die mittlere
Potentialschwelle ueberrollt und an der anderen Seite, an der das Potential
gegen Unendlich geht, wieder beginnt zurueck zu rollen. Sollte der Impuls des
Teilchens genau so ausreichen, dass es auf dem Potentialwall den Impuls 0 hat
('liegen bleibt'), so kann es entweder in die eine oder die andere Mulde
zurueckfallen, welches dem sich aufspaltenden Verhalten der Separatrix
entspricht.

c) Fuer B = 0.1 ist das Potential ein angetriebenes und somit zeitabhaengiges.
Daher gibt es im Gegensatz zum Fall B = 0 mehrere verschiedene Bewegungen.
Zum einen waeren dies die geschlossenen Bahnen in den Mulden des Potentials,
welche aber jetzt noch weitere in sich verschlungenere Phasenraumbehnen
aufweisen, aber dennoch periodisch sein koennen. Auch die globalen
geschlossenen Bahnen existieren noch; auch mit zusaetzlichen Verschlingungen
durch die Oszillationen des Potentials. Waehlt man jedoch die Anfangs-
bedingungen um die Potentialschwelle herum (genauer: zwischen den Niveaulinien
-0.75 < H(x,p) < 0.18) so sieht man nur noch chaotisches Verhalten im Phasen-
raum. Im stroboskopischen Bild erkennt man allerdings auch bei einigen von
ihnen ein ansatzweise periodisches Verhalten.

d) Startkoordinaten einer periodischen Trajektorie:
x = 0.688
p = 0.025
"""