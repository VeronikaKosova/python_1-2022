from lib2to3.pgen2 import driver
import re

class Auto:
  def __init__(self, SPZ, znacka, km):
    self.SPZ = SPZ
    self.znacka = znacka
    self.km = km
    self.k_dispozici = True
  def get_info(self):
    return f"Auto {self.SPZ}, typ {self.znacka} má najeto {self.km} km."
  
  def pujc_auto(self):
    if self.k_dispozici == True:
        self.je_k_dispozici = False
        return (f"Potvrzuji zapůjčení vozidla.")
    else:
      return (f"Vozidlo není k dispozici.")

Peugeot = Auto (SPZ="4A2 3020", znacka="Peugeot 403 Cabrio", km=47534)
Škoda = Auto (SPZ="1P3 4747", znacka="Škoda Octavia", km=41253)

vyber_auto = input ("Jaké preferujete vozidlo - Peugeot nebo Škoda?")
if vyber_auto == "Peugeot":
  print(Peugeot.get_info())
  print(Peugeot.pujc_auto())
elif vyber_auto == "Škoda":
  print(Škoda.get_info())
  print(Škoda.pujc_auto())
else:
  print("Vybraný typ auta nemáme v nabídce.")



