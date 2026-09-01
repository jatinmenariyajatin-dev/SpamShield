from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing so your JS frontend can talk to it

# 1. FIXED PATHS: Removed the duplicate "model/" directory nesting
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model and Vectorizer loaded successfully!")
else:
    model, vectorizer = None, None
    print("⚠️ Warning: Model files missing. Run train_model.py first.")

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return jsonify({'error': 'Model not trained or available'}), 500

    # Get the JSON data from the frontend request
    data = request.get_json()
    
    # Using fallback logic safely
    if not data:
        return jsonify({'error': 'No data payload received'}), 400
        
    message = data.get('message', '')

    if not message.strip():
        return jsonify({'error': 'Empty message'}), 400

    try:
        # ML Pipeline: Transform text -> Predict
        transformed_text = vectorizer.transform([message])
        prediction = int(model.predict(transformed_text)[0])  # 0 or 1
        
        # Get probabilities
        probabilities = model.predict_proba(transformed_text)[0]
        confidence = float(probabilities[prediction] * 100)

        # Return result as JSON
        return jsonify({
            'label': 'Spam' if prediction == 1 else 'Ham',
            'confidence': f"{confidence:.2f}%"
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing exception: {str(e)}'}), 400

if __name__ == '__main__':
    # Running on port 5000 matches your overall Hub configuration strategy!
    app.run(port=5000, debug=True)