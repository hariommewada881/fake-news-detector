# AI-Based Fake News Detection System

## 📌 Project Description

The **AI-Based Fake News Detection System** is a machine learning web application that predicts whether a given news article is **REAL NEWS** or **FAKE NEWS**.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to analyze the text of a news article and provide a prediction along with a confidence percentage.

---
# AI-Based Fake News Detection System

## 📌 Project Description

The AI-Based Fake News Detection System is a machine learning web application that predicts whether a given news article is REAL NEWS or FAKE NEWS.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to analyze the text of a news article and provide a prediction along with a confidence percentage.

## 🖥️ Application Screenshot

![AI-Based Fake News Detector](screenshots/home.jpeg)
## 🚀 Live Demo

The project currently runs locally using Flask.

To start the application:

```bash
python app.py

## 🎯 Objective

The main objective of this project is to develop an AI-based system that can automatically classify news articles as real or fake.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression
* Flask
* HTML
* CSS
* JavaScript
* SQLite
* Joblib

---

## 🤖 Machine Learning Workflow

The project follows these steps:

1. Load the Fake News and True News datasets.
2. Add labels to the datasets.
3. Combine both datasets.
4. Shuffle the data.
5. Combine the news title and text.
6. Split the data into training and testing sets.
7. Convert text into numerical features using **TF-IDF Vectorization**.
8. Train a **Logistic Regression** machine learning model.
9. Evaluate the model using accuracy and classification metrics.
10. Save the trained model and TF-IDF vectorizer using Joblib.
11. Use Flask to create a web application.
12. Display the prediction and confidence percentage.
13. Store prediction history in an SQLite database.

---

## 📊 Dataset

The project uses the **ISOT Fake News Dataset**, containing:

* `Fake.csv` – Fake news articles
* `True.csv` – Real news articles

Labels used:

* `0` → Fake News
* `1` → Real News

---

## 🧠 Machine Learning Model

### TF-IDF

**TF-IDF (Term Frequency-Inverse Document Frequency)** converts news text into numerical values that can be understood by the machine learning model.

### Logistic Regression

Logistic Regression is used to classify the news article into two categories:

* Fake News
* Real News

---

## 📈 Model Accuracy

The model achieved approximately:

**98.45% accuracy** on the test data from the dataset used in this project.

> Note: This accuracy is based on the project's dataset and train-test split. It does not guarantee that every real-world news article will be classified correctly.

---

## ✨ Features

* 📰 Enter or paste a news article
* 🤖 AI-based fake/real prediction
* 📊 Confidence percentage
* 📈 Visual confidence bar
* 🗂️ Prediction history
* 🗑️ Clear input option
* 🧹 Clear prediction history
* 🌐 User-friendly web interface
* 💾 SQLite database for storing predictions

---

## 📁 Project Structure

```text
fake-news-detector/
│
├── app.py
├── Fake.csv
├── True.csv
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── history.db
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 4. Install required libraries

```bash
pip install pandas numpy scikit-learn joblib flask
```

---

## ▶️ How to Run the Project

Open the VS Code terminal and activate the virtual environment:

```bash
venv\Scripts\Activate.ps1
```

Then run:

```bash
python app.py
```

The Flask application will start.

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## 🖥️ How the Application Works

1. User enters a news article.
2. The Flask application receives the article.
3. The TF-IDF vectorizer converts the text into numerical features.
4. The trained Logistic Regression model analyzes the features.
5. The system predicts **REAL NEWS** or **FAKE NEWS**.
6. The confidence percentage is displayed.
7. The prediction is stored in the SQLite database.
8. Previous predictions are displayed in the history section.

---

## 🔮 Future Improvements

* Use advanced NLP models such as BERT.
* Improve performance using larger and more diverse datasets.
* Add multilingual fake news detection.
* Add news source verification.
* Add URL-based news analysis.
* Deploy the application online.
* Improve real-world fact verification.

---

## 🎓 Project Purpose

This project was developed as an **AI/ML academic and portfolio project** to demonstrate practical knowledge of:

* Python
* Machine Learning
* NLP
* Data preprocessing
* Model training
* Flask web development
* Database integration

---

## 👩‍💻 Author

**Sunitha**

B.Tech – Computer Science and Engineering (AI & ML)

---

## 📌 Conclusion

The AI-Based Fake News Detection System demonstrates how **Machine Learning and Natural Language Processing** can be combined with a **Flask web application** to classify news articles.

The project provides a simple and user-friendly interface for analyzing news and viewing prediction results.
