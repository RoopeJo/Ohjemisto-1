pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if not syote:
        break
    try:
        luku = float(syote)
        if pienin is None or luku < pienin:
            pienin = luku
        if suurin is None or luku > suurin:
            suurin = luku
    except ValueError:
        print("Syöte pitää olla numero.")

if pienin is not None:
    print(f"Pienin luku: {pienin:.2f}")
    print(f"Suurin luku: {suurin:.2f}")
else:
    print("Et syöttänyt lukua.")