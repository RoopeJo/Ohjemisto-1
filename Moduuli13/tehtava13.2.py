from flask import Flask, jsonify
import mariadb

app = Flask(__name__)


def hae_lentokentta(icao):
    try:
        yhteys = mariadb.connect(
            host='localhost',
            user='root',
            password='Salasana',
            database='flight_game'
        )
        sql = "SELECT name, municipality FROM airport WHERE ident = %s"
        kursori = yhteys.cursor()
        kursori.execute(sql,(icao,))
        rivi = kursori.fetchone()
        kursori.close()
        yhteys.close()

        if rivi:
            return {
                "ICAO":icao,
                "name": rivi[0],
                "municipality": rivi[1]
            }
        else:
            return None

    except mariadb.Error as e:
        print(f"Tietokantavirhe: {e}")
        return None


@app.route("/kenttä/<icao>", methods=["GET"])
def kentta(icao):
    tulos = hae_lentokentta(icao)
    if tulos:
        return jsonify(tulos)


    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3000)