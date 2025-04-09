from flask import Flask, request


app = Flask(__name__)

def onko_alkuluku(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:luku>", methods=["GET"])
def tarkista_alkuluku(luku):
    tulos = onko_alkuluku(luku)
    return ({"Number": luku, "isPrime": tulos})

if __name__ == "__main__":
    if __name__ == '__main__':
        app.run(use_reloader=True, host='127.0.0.1', port=3000)