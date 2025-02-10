import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import joblib

# Load the dataset
try:
    data = pd.read_csv('data/phishing_dataset.csv')  # Ensure the path is correct
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found. Check the path and try again.")
    exit()

# Drop rows where 'Email Text' or 'Email Type' is NaN
data.dropna(subset=['Email Text', 'Email Type'], inplace=True)

# Convert labels to string type and remove empty strings
data['Email Type'] = data['Email Type'].astype(str).str.strip()
data = data[data['Email Type'] != '']  # Remove empty labels

# Define features and labels
X = data['Email Text'].astype(str)  # Ensure all text data is string
y = data['Email Type']

# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check for remaining NaNs in y_train
if y_train.isnull().sum() > 0:
    print("Warning: y_train still contains NaN values after cleanup.")
    exit()

# Convert email content into TF-IDF features with bigrams (ngram_range=(1,2))
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Apply SMOTE for class balancing
smote = SMOTE(random_state=42)
X_train_tfidf_resampled, y_train_resampled = smote.fit_resample(X_train_tfidf, y_train)
print("Data balanced using SMOTE.")

# Train a Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_tfidf_resampled, y_train_resampled)

# Train an SVM model
svm_model = SVC(kernel='linear', probability=True, random_state=42)
svm_model.fit(X_train_tfidf_resampled, y_train_resampled)

# Evaluate models
rf_pred = rf_model.predict(X_test_tfidf)
svm_pred = svm_model.predict(X_test_tfidf)

rf_accuracy = accuracy_score(y_test, rf_pred)
svm_accuracy = accuracy_score(y_test, svm_pred)

print(f"Random Forest Accuracy: {rf_accuracy * 100:.2f}%")
print(f"SVM Accuracy: {svm_accuracy * 100:.2f}%")

# Save the best-performing model
best_model = rf_model if rf_accuracy > svm_accuracy else svm_model
model_name = "random_forest_model.pkl" if rf_accuracy > svm_accuracy else "svm_model.pkl"
joblib.dump(best_model, f'models/{model_name}')
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')

print(f"Best model ({model_name}) saved successfully!")
