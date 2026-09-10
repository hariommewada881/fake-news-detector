from flask import Flask, render_template, request, redirect
import joblib
import sqlite3

app = Flask(__name__)

# Load trained model and TF-IDF vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Create database
def create_database():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news TEXT,
            prediction TEXT,
            confidence REAL
        )
    """)

    connection.commit()
    connection.close()


create_database()


# Get prediction history
def get_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, news, prediction, confidence
        FROM predictions
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    result_class = None

    if request.method == "POST":

        news = request.form["news"]

        # Convert news into TF-IDF numbers
        news_tfidf = vectorizer.transform([news])

        # Predict
        result = model.predict(news_tfidf)[0]

        # Get probability
        probabilities = model.predict_proba(news_tfidf)[0]

        if result == 0:
            prediction = "FAKE NEWS"
            confidence = round(probabilities[0] * 100, 2)
            result_class = "fake"

        else:
            prediction = "REAL NEWS"
            confidence = round(probabilities[1] * 100, 2)
            result_class = "real"

        # Save prediction
        connection = sqlite3.connect("history.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO predictions (news, prediction, confidence)
            VALUES (?, ?, ?)
        """, (news, prediction, confidence))

        connection.commit()
        connection.close()

    # Get prediction history
    history = get_history()

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        result_class=result_class,
        history=history
    )


# Clear prediction history
@app.route("/clear-history")
def clear_history():

    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM predictions")

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)