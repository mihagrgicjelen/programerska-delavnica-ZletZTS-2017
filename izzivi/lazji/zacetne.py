### Zacetne naloge
from math import *

#Naloga 0.
#Uporabnik poda stranico kvadrata. Izpiši obseg (4*a) in ploščino (a^2)
a = float(input("Stranica kvadrata? "))
print('Obseg kvadrata:', 4 * a)
print('Ploscina kvadrata:', a * a)


#Naloga 1.
#Uporabnik poda polmer kroga. Izpisi obseg (2*pi*r) in ploscino (pi*r^2) kroga.
r = float(input("Polmer kroga? "))
print('Obseg kroga:', 2 * pi * r)
print('Ploscina kroga:', pi * r**2)


#Naloga 2.
#Ana, Bor in Cene naj povedo svoje višine. Izpisi povprecje.
a = float(input("Visina Ane? "))
b = float(input("Visina Bora? "))
c = float(input("Visina Ceneta? "))

print('Povprecje:', (a+b+c)/3)


#Naloga 3.
#Uporabnik poda dolžino prve in druge katete v pravokotnem trikotniku.
#Izpisi hipotenuzo (namig: pitagorov izrek)
k1 = float(input('Kateta? '))
k2 = float(input('Kateta? '))
print('Hipotenuza:', sqrt(k1**2 + k2**2))
