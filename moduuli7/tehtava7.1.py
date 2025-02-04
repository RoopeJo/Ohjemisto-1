def määritä_vuodenaika(kuukausi):
    vuodenajat = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")

    if 1 <= kuukausi <= 12:
        return vuodenajat[kuukausi-1]
    else:
        return "Virheellinen numero."

try:
    kuukausi = int(input("Anna kuukauden numero (1-12): "))
    print("Vuodenaika on :",määritä_vuodenaika(kuukausi))

except ValueError:
    print("Syötä numero väliltä 1-12.")

