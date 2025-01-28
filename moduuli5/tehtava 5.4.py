kaupungit = []

for i in range(5):
    kysymys = ["ensimmäinen", "toinen","kolmas","neljäs","viimeinen"][i]
    kaupunki = input(f"Anna {kysymys} kaupunki?")

    kaupungit.append(kaupunki)
for kaupunki in kaupungit:
    print(kaupunki)


