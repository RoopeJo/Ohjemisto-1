import mysql.connector
import sqlite3

def hae_lentokentta(icao):
    with sqlite3.connect("lentokentat.db") as yhteys:
        kursori = yhteys.cursor()
        kursori.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
        if tulos := kursori.fetchone():
            print(f"Lentokentän nimi: {tulos[0]}\nSijaintikunta: {tulos[1]}")
        else:
            print("Lentokenttää ei löytynyt.")

icao_koodi = input("Anna ICAO-koodi: ").strip().upper()
hae_lentokentta(icao_koodi)

