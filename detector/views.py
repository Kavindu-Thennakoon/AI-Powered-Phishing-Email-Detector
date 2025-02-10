from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import predict_phishing

def index(request):
    return render(request, 'detector/pages/index.html')


@csrf_exempt
def analyze_email_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email_content = data.get('emailContent', '').strip()

            if not email_content:
                return JsonResponse({'error': 'Email content is empty'}, status=400)

            # Predict phishing status
            is_phishing = predict_phishing(email_content)

            # 🔍 Debugging: Print actual model output
            print(f"🔍 Model Output (Fixed): {is_phishing} (Type: {type(is_phishing)})")

            # ✅ Correct condition: Check integer value
            result = "phishing" if is_phishing == 1 else "legitimate"

            print(f"📤 API Response Sent: {result}")  # Debugging

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


