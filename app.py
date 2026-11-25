
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")

@app.route("/estado")
def estado():
    return {
        "proyecto": "AI CIVIL WAR",
        "servidor": "funcionando",
        "participantes": 6,
        "jurado": "Perplexity"
    }

if __name__ == "__main__":
    print("================================")
    print("     AI CIVIL WAR")
    print("     Servidor Flask activo")
    print("================================")
    app.run(host="127.0.0.1", port=8000, debug=False)
