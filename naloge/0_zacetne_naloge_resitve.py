import math

# ============================= NALOGA 0 ============================= #
a = float(input("Stranica kvadrata? "))
print('Obseg kvadrata:', 4 * a)
print('Ploscina kvadrata:', a * a)


# ============================= NALOGA 1 ============================= #
r = float(input("Polmer kroga? "))
print('Obseg kroga:', 2 * math.pi * r)
print('Ploscina kroga:', math.pi * r**2)


# ============================= NALOGA 2 ============================= #
a = float(input("Visina Ane? "))
b = float(input("Visina Bora? "))
c = float(input("Visina Ceneta? "))

print('Povprecje:', (a+b+c)/3)

# ============================= NALOGA 3 ============================= #
k1 = float(input('Kateta? '))
k2 = float(input('Kateta? '))

print('Hipotenuza:', math.sqrt(k1**2 + k2**2))
