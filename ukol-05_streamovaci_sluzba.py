class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
      return f"Evidujeme pořady: {self.nazev} a žánry: {self.zanr}."

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
      return f"Evidujeme film: {self.nazev}, žánr: {self.zanr}, délka filmu: {self.delka} minut."

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def get_info(self):
      return f"Evidujeme seriál: {self.nazev}, žánr: {self.zanr}, počet epizod: {self.pocet_epizod}."

Hra = Film(nazev="Hra", zanr="Horor", delka= 120 )

Hravi = Serial(nazev="Hraví", zanr="romantický", pocet_epizod= 25, delka_epizody= 45)

typ_videa = input("Preferujete Serial nebo Film?")

if typ_videa == "Serial":
    print(Hravi.get_info())
elif typ_videa == "Film":
    print(Hra.get_info())
else:
    print("Bohužel vámi preferovaný typ videa nemáme k dispozici.")
