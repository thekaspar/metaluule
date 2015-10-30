__author__ = 'ATM'
from vanas6nade_import import kysi_vanas6nad


#küsi kasutajalt input
#tee luuletus:
 #tee esimene rida
#

algs6na = input("Algsõna: ")

vanas6nad = kysi_vanas6nad(algs6na)

for vanas6na in vanas6nad:
    vanas6na_pikkus = len(vanas6na)
    for s6na in vanas6na:
        #kui on vähem kui poole



"""Mees teab, mis mees teeb
teeb suure linna suuga, käega kärbsesittagi""