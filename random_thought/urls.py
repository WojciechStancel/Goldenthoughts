from django.urls import path

from random_thought import views

urlpatterns = [
    path('thought/', views.thought),
]