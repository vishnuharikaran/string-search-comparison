from flask import Flask, render_template, request
from search_algorithms import naive_search, kmp_search, rabin_karp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        text = request.form["text"]
        pattern = request.form["pattern"]

        naive_matches, naive_comp = naive_search(text, pattern)
        kmp_matches, kmp_comp = kmp_search(text, pattern)
        rk_matches, rk_comp = rabin_karp(text, pattern)

        results = {
            "naive": (naive_matches, naive_comp),
            "kmp": (kmp_matches, kmp_comp),
            "rk": (rk_matches, rk_comp)
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
