from pickle import TRUE
import re

tel_cislo_prijemce = input("Zadej číslo příjemce: ")
def overeni(tel_cislo_prijemce):
  if tel_cislo_prijemce !=13:
    print(f"Zadej telefonní číslo ve správném formátu +420: ") 
  else:
    return tel_cislo_prijemce

text_SMS = input("Zadej text SMS: ")
def cena_SMS (text_SMS):
  pocet_znaku = int(len(text_SMS))
  vysledna_cena = 3
  vysledna_cena_1 = (len(text_SMS)/180)*3
  if pocet_znaku <180:
    print(f" Výsledná cena sms je: {vysledna_cena} Kč")
  else:
    print(f" Výsledná cena sms je: {vysledna_cena_1} Kč")

cena_SMS("Ahoj Moniko")