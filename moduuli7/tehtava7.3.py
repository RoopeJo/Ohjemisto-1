lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1) Lisää lentoasema")
    print("2) Hae lentoasema ICAO-koodilla")
    print("3) Lopetetaan ohjelma")

    valinta = input("Anna valinta (1-3): ").strip()

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").strip()
        nimi = input("Anna lentoaseman nimi: ").strip()
        if icao and nimi:
            lentoasemat[icao] = nimi
            print("Lentoaseman {nimi} (ICAO: {icao} lisätty.) ")
        else:
            print("Virheellinen syöte, anna uusi syöte.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("ICAO-koodi ei löytynyt.")

    elif valinta == "3":
        print("Lopetetaan ohjelma.")
        break

    else:
        print("Virheellinen valinta, syötä joku valinnoista 1-3.")

