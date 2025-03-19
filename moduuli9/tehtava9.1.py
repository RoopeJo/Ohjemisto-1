class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto1 = Auto("ABC-123", 142, 0, 0)
print(f"rekisteritunnus on {auto1.rekisteritunnus:s} ja huippunopeus on {auto1.huippunopeus:d} km/h. Auton nopeus {auto1.nopeus} km/h ja ajettuja kilometrejä on {auto1.matka} km.")
