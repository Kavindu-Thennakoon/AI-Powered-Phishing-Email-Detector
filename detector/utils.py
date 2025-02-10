import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model and vectorizer
model = joblib.load('detector/models/phishing_model.pkl')
vectorizer = joblib.load('detector/models/tfidf_vectorizer.pkl')

def predict_phishing(email_content):
    """
    Predict if an email is phishing or safe.
    Args:
        email_content (str): The content of the email.
    Returns:
        int: 1 for phishing, 0 for safe.
    """
    # Transform the email content using the vectorizer
    email_vectorized = vectorizer.transform([email_content])

    # Make a prediction
    prediction = model.predict(email_vectorized)[0]  # Extract single value
    print(f"🔍 Model Prediction Output: {prediction}")

    # Ensure return value is an integer (1 for phishing, 0 for safe)
    return 1 if prediction == "Phishing Email" else 0
