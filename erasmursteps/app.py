from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "API Ana Sayfası. /api/merhaba rotasını deneyin."

@app.route("/api/merhaba")
def merhaba():
    return jsonify({"mesaj": "Merhaba dünya! API çalışıyor!"})

if __name__ == "__main__":
    app.run(debug=True)
