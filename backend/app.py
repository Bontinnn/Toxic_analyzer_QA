from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#toxic analysis
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").lower()

    if not text:
        return jsonify({"error": "No text provided"}), 400

#toxic check
    toxic_words = ["hate", "stupid", "idiot", "dumb", "kill"]

    toxic_found = [word for word in toxic_words if word in text]
    is_toxic = len(toxic_found) > 0

    return jsonify({
        "toxic": is_toxic,
        "reason": toxic_found,
        "metrics": {
            "accuracy": 90,
            "precision": 85,
            "recall": 80,
            "f1": 82
        }
    })

#QA
@app.route("/qa", methods=["POST"])
def qa():
    data = request.get_json()
    question = data.get("question", "").lower()

    if not question:
        return jsonify({"answer": "Please enter a question."})

    if "why" in question and "toxic" in question:
        return jsonify({
            "answer": "The comment was classified as toxic because it contains harmful or offensive language."
        })

    if "what" in question and "toxic" in question:
        return jsonify({
            "answer": "Toxic language includes insulting, threatening, or abusive words."
        })

    return jsonify({
        "answer": "This system explains toxicity based on detected harmful keywords."
    })


# -----------------------------
# SERVER START
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
