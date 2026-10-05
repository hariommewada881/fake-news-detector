# AI-Based Fake News Detection System

## 📌 Project Overview

The **AI-Based Fake News Detection System** is a Machine Learning and Natural Language Processing (NLP) based web application that analyzes news articles and predicts whether the given news is **REAL NEWS** or **FAKE NEWS**.

The application provides a simple web interface where users can enter a news article and receive a prediction along with the model's confidence score.

---

## 🎓 Academic Submission Note

This project was selected from an existing open-source GitHub project as part of an academic project assignment.

The project was:

- Set up and executed locally.
- Tested successfully using the Flask web application.
- Customized and improved for academic submission.
- Published in a separate GitHub repository.
- Documented with project details and usage instructions.

The original project attribution and license have been retained.

**Original Project:**  
https://github.com/Suni-sunitha/fake-news-detector

---

## 🎯 Objectives

The main objectives of this project are:

1. To understand the application of Machine Learning in fake news detection.
2. To use Natural Language Processing for analyzing news text.
3. To extract useful text features using TF-IDF.
4. To classify news articles as real or fake.
5. To provide predictions through a user-friendly Flask web application.
6. To understand how an existing Machine Learning project can be deployed and customized.

---

## ✨ Features

- 📰 Fake News / Real News classification
- 🤖 Machine Learning based prediction
- 📝 Natural Language Processing
- 📊 TF-IDF text feature extraction
- 📈 Prediction confidence score
- 📋 Prediction history
- 🧹 Clear input option
- 🔄 Clear prediction history
- 🔢 Live character counter
- ℹ️ About Project section
- 🌐 Flask-based web interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application framework |
| Scikit-learn | Machine Learning |
| NLP | Text processing |
| TF-IDF | Text feature extraction |
| Pandas | Dataset processing |
| NumPy | Numerical operations |
| Joblib | Model serialization |
| HTML | Web page structure |
| CSS | Web page styling |
| SQLite | Prediction history storage |

---

## 🔄 Machine Learning Workflow

The system follows the following workflow:

```text
News Article
     ↓
Text Preprocessing
     ↓
TF-IDF Feature Extraction
     ↓
Trained Machine Learning Model
     ↓
Prediction
     ↓
REAL NEWS / FAKE NEWS
     ↓
Confidence Score
📂 Dataset

The project uses the ISOT Fake News Dataset, containing examples of real and fake news articles.

The dataset files included in the project are:

Fake.csv
True.csv

These datasets are used for training/testing the Machine Learning model.

📁 Project Structure
fake-news-detector/
│
├── screenshots/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
├── app.py
├── Fake.csv
├── True.csv
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── history.db
├── requirements.txt
├── LICENSE
└── README.md
⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/hariommewada881/fake-news-detector.git
2. Open the Project Folder
cd fake-news-detector
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Flask Application
python app.py
5. Open the Application

Open the following address in a web browser:

http://127.0.0.1:5000
🧪 Testing

The application was tested locally by entering different news articles into the input box.

The system returns:

Prediction: REAL NEWS
Confidence: XX.XX%

or

Prediction: FAKE NEWS
Confidence: XX.XX%

The prediction result is displayed directly on the web interface.

🔧 Customizations Made

For the academic submission, the original project was customized and tested locally.

The following improvements were made:

1. User Interface Customization

The main heading and descriptions were updated to provide a more professional project interface.

2. About Project Section

An About This Project section was added to explain the purpose, Machine Learning approach, and technologies used.

3. Live Character Counter

A live character counter was added to the news input area.

The counter automatically updates as the user enters or removes text.

Example:

Characters: 125
4. Improved User Interaction

The input and prediction interface was updated with clearer button labels and instructions.

📊 Model Performance

The original project reports approximately 98.45% test accuracy under its stated dataset and evaluation setup.

Actual performance can vary depending on the dataset, preprocessing, training process, and evaluation methodology.

Therefore, the reported accuracy should not be considered a guarantee of performance on new or unseen news articles.

🎓 Learning Outcomes

Through this project, the following concepts were practiced:

Python programming
Machine Learning
Natural Language Processing
Text classification
TF-IDF feature extraction
Flask web development
Model deployment
Git and GitHub
Project customization
Testing and debugging
🚀 Future Improvements

Possible future improvements include:

Adding more recent news datasets.
Improving text preprocessing.
Testing multiple Machine Learning algorithms.
Adding deep learning models.
Improving the user interface.
Adding multilingual fake news detection.
Improving prediction explainability.
Deploying the application on a cloud platform.
📌 Project Purpose

This project demonstrates how Machine Learning and NLP can be applied to the problem of detecting potentially fake news.

It also provides practical experience in taking an existing open-source project, setting it up locally, understanding its components, making modifications, testing the application, and maintaining the modified version using GitHub.

📜 Original Project Attribution

This academic submission is based on the following original open-source project:

Suni-sunitha/fake-news-detector

https://github.com/Suni-sunitha/fake-news-detector

The original attribution and project license have been retained.

✅ Conclusion

The AI-Based Fake News Detection System provides a simple way to classify news articles using Machine Learning and Natural Language Processing.

The project was successfully configured, tested, customized, and maintained in a separate GitHub repository for academic submission.


### Ab tumhe kya karna hai

VS Code me:

**`fake-news-detector → README.md`**

open karo → **Ctrl + A** → upar wala पूरा content paste karo → **Ctrl + S**.

Uske baad terminal me:

```powershell
git status