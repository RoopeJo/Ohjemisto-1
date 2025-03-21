class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

if __name__ == "__main__":
    hissi = Hissi(1, 10)  # Luodaan hissi, jonka alin kerros on 1 ja ylin 10

    print("Siirretään hissi kerrokseen 5:")
    hissi.siirry_kerrokseen(5)

    print("Siirretään hissi takaisin alimpaan kerrokseen:")
    hissi.siirry_kerrokseen(hissi.alin_kerros)
