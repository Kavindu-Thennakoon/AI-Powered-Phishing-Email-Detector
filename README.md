# 🌐 AI-Powered Phishing Email Detector

An intelligent phishing email detection system powered by machine learning, built with Django. Effortlessly classify emails as **phishing** or **legitimate** with an intuitive web interface.

---

## 📋 Table of Contents
1. [✨ Features](#-features)  
2. [⚙️ Installation](#%EF%B8%8F-installation)  
3. [🚀 Running the Project](#-running-the-project)  
4. [📂 Project Structure](#-project-structure)  
5. [🛠️ How It Works](#%EF%B8%8F-how-it-works)  
6. [🤝 Contributing](#-contributing)  
7. [📜 License](#-license)  
8. [🏆 Acknowledgments](#-acknowledgments)  
9. [📧 Contact](#-contact)  

---

## ✨ Features  
- 🚨 **Phishing Detection**: Leverages machine learning to detect phishing attempts effectively.  
- 🖥️ **User-Friendly Interface**: A sleek web interface built using Django for seamless user interaction.  
- 🔧 **Customizable**: Extendable to include additional features or enhanced models.  
- 🛠️ **Admin Panel**: Manage detection history and system configurations through the Django admin dashboard.  

---

## ⚙️ Installation  

### Prerequisites  
- Python 3.8 or higher  
- pip (Python package manager)  

### Steps  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Hasendra1/AI-Powered-phishing-email-detector.git
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**  
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**  
   ```bash
   python manage.py runserver 8080
   ```

---

## 🚀 Running the Project  
After completing the installation, open your browser and navigate to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 📂 Project Structure  

```
AI-Powered-phishing-email-detector/
├── phishing_detector/               # Django project folder
│   ├── __init__.py
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── detector/                        # Django app folder
│   ├── migrations/                  # Database migrations
│   ├── __init__.py
│   ├── admin.py                     # Admin configurations
│   ├── apps.py
│   ├── models.py                    # Database models
│   ├── tests.py
│   ├── views.py                     # Application logic
│   ├── phishing_model.pkl
│   ├── vectorizer.pkl
│   ├── static/                      # Static files (CSS, JS, images)
│   │   └──detector/
│   │      ├── css/
│   │      ├── images/
│   │      └── js/
│   └── templates/                   # HTML templates
│       └── detector/
│           ├── layout/ 
│           │   ├── header.html
│           │   ├── nav.html
│           │   └── footer.html
│           ├── pages/ 
│           │   └── index.html
│           └── base.html        
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── LICENSE                          #  Project license
└── README.md                        # Project documentation
```

---

## 🛠️ How It Works  

### 🔗 Input Email Text  
Users paste the email content into the form on the web interface.  

### 🧹 Preprocessing  
The text is vectorized using a **TF-IDF vectorizer** to match the format used during training.  

### 🧠 Prediction  
The preprocessed data is fed into the **machine learning model** to classify the email as **phishing** or **legitimate**.  

### 📊 Result Display  
Results are displayed instantly, providing clear feedback to the user.  

---

## 🤝 Contributing  

Contributions are welcome! Here's how you can help:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push the branch:  
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request on GitHub.  

---

## 📜 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

---

## 🏆 Acknowledgments  
- [Django](https://www.djangoproject.com/): For the web framework.  
- [Scikit-learn](https://scikit-learn.org/): For the machine learning tools.  
- [Kaggle](https://www.kaggle.com/): For the phishing email dataset.  

---

## 📧 Contact  

For questions or feedback, reach out to:  
**[Your Name]**  
- GitHub: [Your GitHub Profile](https://github.com/YourGitHubProfile)  
- Email: your.email@example.com  

---

