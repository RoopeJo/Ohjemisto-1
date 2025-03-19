class Auto:
    def __init__(self, huippunopeus,):
        self.huippunopeus = huippunopeus
        self.nopeus = 0

    def kiihdyta (self, muutos):
        uusi_nopeus = self.nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
           self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
             self.nopeus = 0
        else:
             self.nopeus = uusi_nopeus

auto = Auto(142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton uusi nopeus on {auto.nopeus} km/h")

auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto.nopeus} km/h")