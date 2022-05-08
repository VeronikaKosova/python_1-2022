from dataclasses import replace
from enum import auto
from re import X
from string import printable

with open("auta.txt", encoding="utf-8") as vstup:
  auta = vstup.readlines()
print(auta)
auta = [SPZ.split(" ") for SPZ in auta]
# print(auta)
pocet_km = 0.0
for SPZ in auta:
  pocet_km += float(SPZ[1].replace(",", "."))
print(f"Vozidla najela celkem: {pocet_km} km.")

