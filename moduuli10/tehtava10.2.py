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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissi {hissi_numero + 1} kerrokseen {kohde_kerros}.")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissinumero ei kelpaa.")

if __name__ == "__main__":
    talo = Talo(1, 10, 3)  # Luodaan talo, jossa on 3 hissiä

    print("Ajetaan ensimmäinen hissi kerrokseen 5:")
    talo.aja_hissiä(0, 5)

    print("Ajetaan toinen hissi kerrokseen 8:")
    talo.aja_hissiä(1, 8)

    print("Palautetaan ensimmäinen hissi alimpaan kerrokseen:")
    talo.aja_hissiä(0, talo.hissit[0].alin_kerros)