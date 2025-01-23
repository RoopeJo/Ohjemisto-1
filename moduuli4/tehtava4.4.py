import random
salainen_luku = random.randint(1,10)

print("Arvaa luku väliltä 1 - 10")

while True:
    arvaus = int(input("Syötä arvaus:"))
    if arvaus < salainen_luku:
        print("Liian pieni luku")
    elif arvaus > salainen_luku:
        print("Liian suuri luku")
    else:
        print("Oikea arvaus!")
        break