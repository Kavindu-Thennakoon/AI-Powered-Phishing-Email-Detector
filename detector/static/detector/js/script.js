document.addEventListener('DOMContentLoaded', function () {
    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Handle Form Submission
    const emailForm = document.getElementById('emailForm');
    const resultSection = document.getElementById('results');
    const resultText = document.getElementById('resultText');
    const resultIcon = document.getElementById('resultIcon');
    const resultCard = resultSection.querySelector('.result');
    const emailContentInput = document.getElementById('emailContent');

    // Initially hide the results section
    resultSection.style.display = 'none';

    emailForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent default form submission

        // Clear previous results
        resultText.innerHTML = "Analyzing your email...";
        resultText.style.color = "#fff";
        resultIcon.classList.remove('fa-exclamation-circle', 'fa-check-circle');
        resultIcon.classList.add('fa-question-circle');
        resultCard.classList.remove('phishing', 'legitimate');

        // Get the email content
        const emailContent = emailContentInput.value;

        // Send the data to the server using AJAX
        fetch('/analyze/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // Include CSRF token
            },
            body: JSON.stringify({ emailContent: emailContent }),
        })
        .then(response => response.json())
        .then(data => {
            // Display the result
            if (data.result === "phishing") {
                resultIcon.classList.remove('fa-question-circle');
                resultIcon.classList.add('fa-exclamation-circle');
                resultText.innerHTML = "🚨 <strong>This email is PHISHING!</strong>";
                resultCard.classList.add('phishing');
                resultCard.classList.remove('legitimate');
            } else if (data.result === "legitimate") {
                resultIcon.classList.remove('fa-question-circle');
                resultIcon.classList.add('fa-check-circle');
                resultText.innerHTML = "✅ <strong>This email is LEGITIMATE.</strong>";
                resultCard.classList.add('legitimate');
                resultCard.classList.remove('phishing');
            }

            // Show the results section
            resultSection.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });

        // Reset the form after submission
        emailForm.reset();
    });
});
