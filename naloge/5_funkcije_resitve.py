
# ============================= NALOGA 1 ============================= #

def obseg_trikotnika(a, b, c):
    obseg = a + b + c
    return obseg

# ============================= NALOGA 2 ============================= #

def vsota_seznama(sez):
    vsota = 0
    for x in sez:
        vsota += x
    return vsota

# ============================= NALOGA 3 ============================= #

def pozdrav(ime_priimek):
    print('Pozdravljen nadobudni astronavt %s!' % ime_priimek)