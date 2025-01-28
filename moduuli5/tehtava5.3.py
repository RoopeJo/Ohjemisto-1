luku = int(input("Anna kokonaisluku:"))

if luku < 2:
    print(f"Luku {luku} ei ole alkuluku.")
else:
    for i in range(2,luku):
        if luku % i == 0:
            print(f"Luku {luku} ei ole alkuluku.")
            break

    else:
        print(f"Luku {luku} on alkuluku.")