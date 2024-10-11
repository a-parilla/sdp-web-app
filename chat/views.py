from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        # For now, return a placeholder response
        response_message = "Hello! How can I assist you today?"
        return JsonResponse({'response': response_message})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
