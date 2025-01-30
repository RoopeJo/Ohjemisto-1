import random

def nopan_heitto(tahko):
    return random.randint(1, tahko)

tahko = int(input("Monta tahkoa nopassa on?:"))
while True:
    tulos = nopan_heitto(tahko)
    print(f"Heiton tulos:{tulos}")
    if tulos == tahko:
        break
