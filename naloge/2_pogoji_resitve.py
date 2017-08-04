
# ============================= NALOGA 1 ============================= #

vnesena_temp = float(raw_input('Vnesi temperaturo: '))
if vnesena_temp > 30:
    print('Toooooplo je, pejdi se okopat v jezero!')
else:
    print('Its cool!')

# ============================= NALOGA 2 ============================= #

stevilka = int(raw_input('Vnesi stevilko: '))

if stevilka % 2 == 0:
    print('Stevilo %s je SODO!' % stevilka)
else:
    print('Stevilo %s je LIHO!' % stevilka)
