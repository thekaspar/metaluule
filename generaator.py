__author__ = 'ATM'
#from vanas6nade_import import kysi_vanas6nad
from collections import defaultdict

#küsi kasutajalt input
#tee luuletus:
 #tee esimene rida
#


def leia_vanas6nade_parameetrid(v6tmes6na, uued_vanas6nad, parameetrid=defaultdict(list)):
    for vanas6na in uued_vanas6nad:
        s6nad = vanas6na.strip().split()
        s6nad = [s6na.strip(",") for s6na in s6nad]

        vanas6na_pikkus = len(vanas6na)
        #kui on vähem kui poole
        if v6tmes6na in s6nad:
            s6na_indeks = s6nad.index(v6tmes6na)
            #0-1 punkti sõna asetuse eest
            s6na_asetus = (s6na_indeks/vanas6na_pikkus)
            #0-1 punkti vanasõna pikkuse eest
            parameetrid[vanas6na] = [s6na_asetus, vanas6na_pikkus]
    return parameetrid

#kood on kirjutatud pidades silmas, et siina vahel saaks olla kaalude optimeerimise funktsioon

def leia_parim_vanas6na(parameetrid, kaalud=[1,1]):
    max_skoor = 0
    for vanas6na in parameetrid:
        s6na_indeks, vanas6na_pikkus = parameetrid[vanas6na]
        skoor = s6na_indeks*kaalud[0] + vanas6na_pikkus*kaalud[1]
        if skoor > max_skoor:
            max_skoor = skoor
            parim_vanas6na = vanas6na
    return parim_vanas6na

def kirjuta_rida(v6tmes6na):
    #parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, kysi_vanas6nad(v6tmes6na))
    f = open("n2idis_import_tegu.txt")
    lines = f.readlines()
    parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, lines)
    rida = leia_parim_vanas6na(parameetrid)
    s6nad = rida.split()
    viimane_s6na = s6nad[-1]
    return rida, viimane_s6na

#MAIN
#algs6na = input("Algsõna: ")


rida, viimane_s6na = kirjuta_rida("mees")
print(rida)
