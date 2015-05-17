"""
Aufgabe 2.1

Dieses Programm dient dem Kennenlernen elementarer numerischer Integrations-
methoden: der Mittelpunktsmethode, der Trapezmethode und der Simpson-Methode.
Zudem sollen die numerischen Fehler ebenjener Methoden in Abhaengigkeit von der
Intervallbreite der bestimmten Integration dargestellt werden. Testobjekte
werden drei verschieden gutartig zu integrierende Funktionen sein.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def fa(x):
    """
    Gegebene Funktion aus Aufgabenstellung a)
    """
    return np.sin(2*x)
# Analytische Loesung des bestimmten Integrals aus a)
Inta = -0.25


def fb(x):
    """
    Gegebene Funktion aus Aufgabenstellung b)
    """
    return np.exp(-100 * (x**2))
# Genaeherte Loesung des bestimmten Integrals aus b)
Intb = 0.177245385090


def fc(x):
    """
    Gegebene Funktion aus Aufgabenstellung c)
    """
    return (1.0 + np.sign(x))/2
# Analytische Loesung des bestimmten Integrals aus c)
Intc = np.pi/3


def middle(func, a, b, n):
    """
    Berechnet numerisch mittels der Mittelwertmethode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float((b - a)/n)                    # Intervallbreite
    x_i = np.linspace(a, b, n, endpoint=False)  # Erzeugung eines Arrays linker
    f_i = func(x_i + width/2)                   # Grenzen, Funktionswerte
    return sum(f_i) * width                     # werden in der Mitte genommen


def trapez(func, a, b, n):
    """
    Berechnet numerisch mittels der Trapezmethode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float(b - a)/n
    x_i = np.linspace(a, b, n + 1)              # Erzeugung eines Arrays linker
    f_i = (func(x_i[:-1]) + func(x_i[1:]))/2    # und rechter Grenzen, Fktwerte
    return sum(f_i) * width                     # zwischen beiden gemittelt


def simpson(func, a, b, n):
    """
    Berechnet numerisch mittels der Simpson-Methode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float(b - a)/(2*n)                  # halbe Breite
    x = np.linspace(a, b, 2*n + 1)              # Fktwerte wie Trapezmethode,
    f_i = (func(x[:-1]) + func(x[1:]))/2        # einmal halbe und ganze Breite
    f_j = (func(x[:-2:2]) + func(x[2::2]))/2    # mit entspr. Wichtung
    return 4/3 * sum(f_i) * width - 1/3 * sum(f_j) * width * 2

# Minimale Benutzerfuehrung
print __doc__

# feste obere und untere Integrationsgrenze als Parameter
A = -np.pi/2
B = np.pi/3

# Anzahl der verschiedenen Intervallanzahlen (int32) in logarithmischen Abstand
# allerdings Doppelung durch Rundung, mit np.unique() herausgefiltert
number = 1000
N_list = np.unique(np.int32(np.logspace(0, 5, number)))

# Intervallbreiten aus der Anzahl der Intervalle
h_list = (B - A)/N_list

# Arrays fuer die Betraege der relativen Fehler der drei Methoden
error_middle = np.zeros(len(N_list))
error_trapez = np.zeros(len(N_list))
error_simpson = np.zeros(len(N_list))

# Befuellen der Fehlerlisten innerhalb einer Schleife. Dies ist noetig, da
# innerhalb der Funktionen nicht ohne grossen Aufwand der Typ ndarray in den
# Aufruf von np.linspace() einzubetten ist
for z in range(len(N_list)):
    error_middle[z] = np.absolute((middle(fa, A, B, N_list[z]) - Inta)/Inta)
    error_trapez[z] = np.absolute((trapez(fa, A, B, N_list[z]) - Inta)/Inta)
    error_simpson[z] = np.absolute((simpson(fa, A, B, N_list[z]) - Inta)/Inta)


# Anlegen eines Plotfensters mit logarithmischer Achseneinteilung
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, xscale='log', yscale='log')

# Plotten der Fehler der verschiedenen Methoden als Punktplot
ax.plot(h_list, error_middle, 'g.', ms=2, label='Mittelwertmethode')
ax.plot(h_list, error_trapez, 'r.', ms=2, label='Trapezmethode')
ax.plot(h_list, error_simpson, 'b.', ms=2, label='Simpson-Methode')

# Plotten des Skalierungsverhaltens fuer die Methoden. Damit dadurch nicht der
# Plotbereich verzerrt wird, wird nur eine kuerzere Linie mittels des
# angelegten Arrays x gezeichnet
x = np.logspace(-3, -1, 100)
ax.plot(x, x**2, 'k--', label='Skalierungsverhalten: $h^2$')
ax.plot(x, x**4, 'b--', label='Skalierungsverhalten: $h^4$')

# Anzeigen der Legende an der bestmoeglichen Position
ax.legend(loc='best')
ax.set_xlabel('$h$', fontsize=18)
ax.set_ylabel(r"$\frac{\Delta I}{I}$", fontsize=18)
ax.set_title('Numerische Integration', fontsize=20)

plt.show()

"""
Beobachtung:

a) Das hier gegebene bestimmte Integral war analytisch leicht zu loesen und
lieferte ein Ergebnis von -0.25.
Wie zu erwarten lieferte die Simpson-Methode das genaueste Ergebnis, welches
nur einen Fehler von ~7.5e-14 bei einer Intervallbreite von 0.0018 aufwies.
Damit ist es auch die effizienteste Methode was die Rechenzeit angeht, da
weniger, groessere Intervalle berechnet werden muessen. Allerdings sieht man
auch, dass die Simpson-Methode bei immer kleiner werdenden Breiten nicht
besser wird, sondern ihr Fehler zu rauschen beginnt. Dies liegt an der
Differenzbildung bei der Berechnung des relativen Fehlers, da die errechnete
Differenz zu nah an der Null liegt und somit  Probleme mit der genauen
Aufloesung das Rauschen verursachen.
Die Mittelwertmethode waere die naechstgenauere Methode mit einem minimalen
Fehler von ~1e-10 bei einer Intervallbreite von 2.6e-5 (im untersuchten
Bereich!). Die Trapezmethode hat ihren kleinsten Fehler von ~2.3e-10 bei einer
Breite von 2.6e-5. Beide letztgenannten Methoden skalieren mit h^4, waehrend
die Simpson-Methode mit h^4 skaliert.
Versucht man die Intervalle noch kleiner zu machen, um die minimalen Fehler der
Trapez- und Mittelwertsmethode zu ermitteln, so gelangt man schnell zu grossen
Rechenzeiten. In der Tat dauerte dies bei mir so lang, dass ich das Programm
abbrach, bevor es ein Ergebnis erzielte.

b) Das hier zu berechnende bestimmte Integral liess sich nicht exakt analytisch
berechenen, daher habe ich unter Zuhilfenahme von Wolfram Alpha folgende
genaeherte Loesung genutzt: 0.177245385090.
Plottet man die Funktion einmal, um sie genauer zu betrachten, faellt einem
auf, dass sie sehr steile Anstiege zu beiden Seiten der Null hat, also quasi
fast einer Delta-Distribution entspricht.
Damit laesst sich auch das merkwuerdige Verhalten der drei Integrationsmethoden
erklaeren, welche sich alle einen sehr aehnlichen Verlauf in Abhaengigkeit von
der Intervallbreite zeigen: Zunaechst weisen sie mit bis zu ~2e1 einen sehr
grossen Fehler auf, fallen dann aber (bis zu einer Breite von 0.006) sehr
schnell auf einen bis zum Ende konstant bleibenden Wert von 3.2e-12 ab. Der
starke Abfall zu Beginn laesst sich mit dem starken Anstieg der Funktion
erklaeren: eine kleine Variation aufder x-Achse verursacht eine grosse
Verschiebung auf der y-Achse, sodass die Integrationsrechtecke und ~trapeze
kaum etwas mit der wahren Funktion gemein haben. Hat man dann allerdings diesen
kritischen Bereich um die Null herum genau genug genaehert, gibt es mit dem
restlichen Definitionsbereich nur wenig Probleme, sodass der Fehler konstant
niedrig bleibt.

c) Das hier gegebene bestimmte Integral liess sich aufgrund der Eigenschaften
der Theta-Funktion wieder relativ einfach analytisch loesen; das Ergebnis
lautet wenig ueberraschend pi/3.
Umso interessanter ist das Verhalten der drei Integrationsmethoden, welche sich
auch hier alle sehr gleich verlaufen: Ihre Fehler 'springen' zwischen jeweils
drei mit h^1 abfallenden Geraden hin und her. Dies laesst sich jedoch leicht
durch die Unstetitigkeitsstelle an der null erklaeren, da die gewaehlten
Intervalle immer abwechseln asymmetrisch und symmetrisch auf ihr liegen.


Zusammenfassend muss man sagen, dass man, wenn man eine numerisch Integrations-
methode anwendet von Funktion zu Funktion ueberpruefen muss, ob das gelieferte
Ergebnis sinnvoll erscheint, da nicht jede Funktion so gutartig ist, wie die in
a) gegebene.
"""