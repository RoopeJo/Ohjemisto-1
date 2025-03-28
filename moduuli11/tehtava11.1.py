class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi,kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja:{self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä:{self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja:{self.paatoimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_numero_6 = Kirja ("Hytti numero 6", "Rosa Liksom",200)


aku_ankka.tulosta_tiedot()
print()
hytti_numero_6.tulosta_tiedot()