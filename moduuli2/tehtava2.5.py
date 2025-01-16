# Määritellään vakioarvot
yksi_leiviska_nauloina = 20
yksi_naula_luoteina = 32
yksi_luoti_grammoina = 13.3

def muunna_kilogrammoiksi_ja_grammoiksi(leiviskat, naulat, luodit):
    kokonaismassa_grammoina = (
        leiviskat * yksi_leiviska_nauloina * yksi_naula_luoteina * yksi_luoti_grammoina +
        naulat * yksi_naula_luoteina * yksi_luoti_grammoina +
        luodit * yksi_luoti_grammoina
    )
    kilogrammat = int(kokonaismassa_grammoina // 1000)
    grammat = kokonaismassa_grammoina % 1000
    return kilogrammat, grammat

if __name__ == "__main__":
    try:
        leiviskat = int(input("Anna leivisköiden määrä leivisköinä: "))
        naulat = int(input("Anna naulojen määrä nauloina: "))
        luodit = int(input("Anna luotien määrä luoteina: "))
        kilogrammat, grammat = muunna_kilogrammoiksi_ja_grammoiksi(leiviskat, naulat, luodit)
        print(f"Massa on {kilogrammat} kilogrammaa ja {grammat:.1f} grammaa.")
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaislukuja.")








