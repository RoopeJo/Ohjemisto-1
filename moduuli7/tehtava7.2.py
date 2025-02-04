def nimi_lista():
    nimet = set()
    while True:
        nimi = input("Syötä nimi(tyhjä merkkijono lopettaa): ").strip()

        if nimi in nimet:
            print("Nimi on jo syötetty")
        if nimi == "":
            break
        else:
            nimet.add(nimi)

    print("\nSyötetyt nimet:")
    for nimi in nimet:
        print(nimi)

nimi_lista()