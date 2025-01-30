def gallonat_litroiksi(gallona):
    return gallona * 3.785

määrä = float(input("Kuinka monta gallonia bensiinia on?"))

if määrä < 0:
    print("Ei bensaa jäljellä")

litrat = gallonat_litroiksi(määrä)
print(f"{määrä} gallonaa on {litrat:.2f} litraa")



