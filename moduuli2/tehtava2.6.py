import random

def arvo_kolmenumeroinen_koodi():
    return "".join(str(random.randint(0, 9)) for _ in range(3))

def arvo_nelinumeroinen_koodi():
    return "".join(str(random.randint(1, 6)) for _ in range(4))

if __name__ == "__main__":
    kolmenumeroinen_koodi = arvo_kolmenumeroinen_koodi()
    nelinumeroinen_koodi = arvo_nelinumeroinen_koodi()

    print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
    print(f"Nelinumeroinen koodi: {nelinumeroinen_koodi}")