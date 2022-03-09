
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cislo_baliku = input("Zadejte číslo balíku: ")
if cislo_baliku in baliky:
  if baliky[cislo_baliku] == True:
    print(f"Balík {cislo_baliku} byl předán kurýrovi.")
  if baliky[cislo_baliku] == False:
    print(f"Balík {cislo_baliku} zatím nebyl předán kurýrovi.")

