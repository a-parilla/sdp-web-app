from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('upload/', views.upload_document, name='upload_document'),
]
