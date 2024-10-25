from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import Document

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

# Adapted from https://docs.djangoproject.com/en/5.1/topics/http/file-uploads/
@login_required
@csrf_exempt
def upload_document(request):
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['file']) 
            newdoc.save()

            return redirect('')
        else:
            return JsonResponse({'error': 'Invalid file form.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
