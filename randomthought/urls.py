from django.urls import path

from randomthought import views

urlpatterns = [
    path('thought/', views.thought),
]