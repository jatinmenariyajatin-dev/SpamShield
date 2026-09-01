# 🛡️ SpamShield – AI-Based Spam Message Detection

SpamShield is a **Machine Learning and NLP-based spam message detection system** that analyzes text messages and classifies them as **Spam** or **Ham (Not Spam)**.

The project uses a trained Machine Learning model, a text vectorizer, and a **Flask REST API** to provide real-time spam detection with a confidence score.

---

## 🚀 Features

* 📩 Detects whether a message is **Spam** or **Ham**
* 🤖 Uses Machine Learning for text classification
* 🧠 NLP-based text vectorization
* 📊 Provides prediction confidence
* 🌐 Flask REST API
* 🔗 CORS enabled for frontend integration
* ⚡ Real-time prediction
* 💾 Uses Joblib for loading trained ML models

---

## 🛠️ Technologies Used

* **Python**
* **Machine Learning**
* **Natural Language Processing (NLP)**
* **Scikit-learn**
* **Flask**
* **Flask-CORS**
* **Joblib**
* **REST API**

---

## 📁 Project Structure

```text
SpamShield/
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── server.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```text
User Message
     ↓
Frontend
     ↓
Flask REST API
     ↓
Text Vectorization
     ↓
Machine Learning Model
     ↓
Spam / Ham Prediction
     ↓
Confidence Score
     ↓
JSON Response
```

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project

```bash
cd SpamShield
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Before running the API, make sure the trained model files are available inside the `model` folder.

Run:

```bash
python train_model.py
```

The training process should generate:

```text
model/
├── spam_model.pkl
└── vectorizer.pkl
```

---

## ▶️ Run the Flask API

Start the server using:

```bash
python server.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoint

### Predict Spam

**Endpoint:**

```text
POST /predict
```

### Request

Send JSON data containing the message:

```json
{
    "message": "Congratulations! You have won a free prize."
}
```

### Response – Spam

```json
{
    "label": "Spam",
    "confidence": "98.45%"
}
```

### Response – Ham

```json
{
    "label": "Ham",
    "confidence": "96.72%"
}
```

---

## ❌ Error Handling

SpamShield handles common API errors such as:

### No Data

```json
{
    "error": "No data payload received"
}
```

### Empty Message

```json
{
    "error": "Empty message"
}
```

### Model Not Available

```json
{
    "error": "Model not trained or available"
}
```

---

## 🔍 Model Files

SpamShield requires two trained files:

| File             | Purpose                               |
| ---------------- | ------------------------------------- |
| `spam_model.pkl` | Trained spam classification model     |
| `vectorizer.pkl` | Converts text into numerical features |

The Flask application automatically checks whether these files exist before loading them.

---

## 📌 Example Messages

### Spam

```text
Congratulations! You won a free lottery ticket. Claim now!
```

Prediction:

```text
Spam
```

### Ham

```text
Hey, are we meeting at 6 PM today?
```

Prediction:

```text
Ham
```

---

## 🔐 CORS Support

SpamShield uses **Flask-CORS** to allow communication between the Flask backend and a separate JavaScript/frontend application.

```python
CORS(app)
```

This makes it suitable for integration with web-based frontend applications.

---

## 📈 Future Improvements

* Add a modern web interface
* Improve model accuracy
* Add multiple spam categories
* Store prediction history
* Add user authentication
* Deploy API to a cloud platform
* Add advanced NLP techniques
* Add model performance dashboard

---

## 🎯 Project Objective

The main objective of SpamShield is to build an automated system capable of identifying unwanted or potentially harmful messages using **Machine Learning and Natural Language Processing**.

It demonstrates the integration of:

**ML Model → NLP Vectorization → Flask API → Frontend**

---

## 👨‍💻 Author

**Jatin Menariya**

---

## ⭐ Project Highlights

> **SpamShield** is a practical Machine Learning project that combines **NLP, text classification, Flask REST API, and real-time prediction** into a single application.

If you find this project useful, consider giving the repository a ⭐.
