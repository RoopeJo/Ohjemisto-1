class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def aseta_nopeus(self, uusi_nopeus):
        if 0 <= uusi_nopeus <= self.huippunopeus:
            self.nopeus = uusi_nopeus
        else:
            print("Virheellinen nopeus!")

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aseta_nopeus(120)
polttomoottoriauto.aseta_nopeus(150)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print(f"Sähköauton rekisteritunnus on ({sahkoauto.rekisteritunnus}) ja matkamittari näyttää: {sahkoauto.matka} km")
print(f"Polttomoottoriauton rekisteritunnus on ({polttomoottoriauto.rekisteritunnus}) ja matkamittari näyttää : {polttomoottoriauto.matka} km")