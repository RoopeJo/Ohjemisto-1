luvut = []

while True:
    syote = input("Anna luku tai lopeta painamalla Enter: ")
    if syote == "":
        break
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Syöte pitää olla numero.")

luvut.sort(reverse=True)

print("Viis isointa lukua ovat:), luku[:5]: ", luvut[:5])
