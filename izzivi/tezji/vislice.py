import random

BESEDE = ['BANANA', 'RAKETA', 'JEZERO']
MAX_ST_NAPAK = 4


def izpisi_besedo(beseda, seznam_uganjenih):
    # Naredimo prazen niz, v katerega bomo dodajali crke oz 'crtice'
    izpis = '\n'

    for i, crka in enumerate(beseda):
        # Za znak na i-tem mestu v besedi, pogledamo na i-to mesto v seznam_uganjenih
        # ali moramo izpisati crtico ali crko.
        if seznam_uganjenih[i] == True:
            izpis += crka
        else:
            izpis += '_'

    # Tale koscek samo doda presledke okoli izpisa. Tole lahko ignoriras
    izpis = '  '.join([x for x in izpis])

    print(izpis)
 

# Izberemo nakljucno besedo iz seznama BESEDE
nakljucni_index = random.randint(0, len(BESEDE) - 1)
nakljucna_beseda = BESEDE[nakljucni_index]

seznam_uganjenih = [False for x in nakljucna_beseda]
stevilo_napak = 0
izpisi_besedo(nakljucna_beseda, seznam_uganjenih)


while True:ss

    vnesena_crka = raw_input('Vnesi crko: ').upper()

    if vnesena_crka in nakljucna_beseda:  # preverimo ali smo uganili pravo crko

        # Crko smo uganili, to si moramo zapomniti (v seznamu_uganjenih)
        for i, crka in enumerate(nakljucna_beseda):
            if crka == vnesena_crka:
                seznam_uganjenih[i] = True
    else:
        stevilo_napak += 1
        print('Joj! Napaka! Ostane ti se %s poskusov' % (MAX_ST_NAPAK - stevilo_napak))

    # Izhodni pogoji
    if stevilo_napak >= MAX_ST_NAPAK:
        print('*** GAME OVER ***')
        break

    if all(seznam_uganjenih) == True:
        print('*** BRAVO!!! ***')
        break

    izpisi_besedo(nakljucna_beseda, seznam_uganjenih)
