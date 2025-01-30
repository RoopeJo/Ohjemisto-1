import random

def nopan_heitto():
    return random.randint(1,6)

while True:
    silmäluku = nopan_heitto()
    print(f"Heiton tulos:{silmäluku}")
    if silmäluku == 6:
        break
