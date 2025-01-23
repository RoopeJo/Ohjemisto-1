while True:
    tuuma = float(input("Anna tuuma määrä(negatiivinen lopettaa): "))
    if tuuma < 0:
        print("lopetettu.")
        break
    print(f"{tuuma} tuumaa on {tuuma * 2.54:.2f} senttimetriä.")