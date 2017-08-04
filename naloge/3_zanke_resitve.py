
# ============================= NALOGA 1 ============================= #

vsota = 0
i = 0

while i < 5:
    cena = int(input('Cena artikla: '))
    vsota += cena
    i += 1

print('Vsota: %s EUR' % vsota)


# ============================= NALOGA 2 ============================= #
vsota = 0
i = 0

stevilo_izdelkov = int(input('Stevilo izdelkov: '))

while i < stevilo_izdelkov:
    cena = int(input('Cena artikla: '))
    vsota += cena
    i += 1

print('Vsota: %s EUR' % vsota)

# ============================= NALOGA 3 ============================= #

vsota = 0
while True:
    cena = int(input('Cena artikla: '))

    if cena == 0:
        break

    vsota += cena

print('Vsota: %s EUR' % vsota)
