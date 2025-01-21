Sukupuoli = input("sukupuoli?").lower().lower()
Hemoglobiiniarvo = int(input("g/l?"))

normaalirajat = {
    "nainen":(117, 175),
    "mies":(134, 195)}

if Sukupuoli in normaalirajat:
    alin, ylin = normaalirajat[Sukupuoli]
    if Hemoglobiiniarvo < alin:
        print("Hemoglobiiniarvo alhainen.")
    elif Hemoglobiiniarvo > ylin:
        print("Hemoglobiiniarvo korkea")
    else:
        print("Hemoglobiiiniarvo normaali.")

