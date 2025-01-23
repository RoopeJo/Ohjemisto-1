vuosi = int(input("Anna vuosi:"))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"vuosi {vuosi} on karkausvuosi.")
else:
    print(f"vuosi {vuosi} ei ole karkausvuosi.")
