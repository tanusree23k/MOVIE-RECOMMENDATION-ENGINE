from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

movies = pd.read_csv("movies.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        genre = request.form["movie"].strip().lower()

        filtered_movies = movies[
            movies["genre"].str.lower() == genre
        ]

        recommendations = filtered_movies["title"].tolist()

        if not recommendations:
            recommendations = ["Genre not found"]

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)