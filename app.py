import webbrowser
from flask import Flask, request, jsonify, render_template
from detector import detect_attack

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    payload = data.get("payload", "")
    if not payload:
        return jsonify({"error": "No payload provided"}), 400
    result = detect_attack(payload)
    return jsonify(result)

if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)  # <-- Automatically opens browser
    app.run(debug=True)


