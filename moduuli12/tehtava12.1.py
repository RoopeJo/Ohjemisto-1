import requests
import json

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(url)
        vastaus.raise_for_status()
        data = vastaus.json()
        print(data["value"])
    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa vitsiä:", e)

if __name__ == "__main__":
    hae_chuck_norris_vitsi()