import mysql.connector

def laske_lentokentat(maakoodi, tiedosto="airports.dat"):
    laskuri = {}
    try:
        with open(tiedosto, encoding="utf-8") as f:
            for rivi in mysql.connector.reader(f):
                if len(rivi) > 5 and rivi[3].upper() == maakoodi.upper():
                    laskuri[rivi[2]] = laskuri.get(rivi[2], 0) + 1
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")
        return {}
    return laskuri

def main():
    maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()
    tulokset = laske_lentokentat(maakoodi)
    if tulokset:
        print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
        for tyyppi, lkm in tulokset.items():
            print(f"{tyyppi}: {lkm}")
    else:
        print("Ei löydetty tietoja.")

if __name__ == "__main__":
    main()
