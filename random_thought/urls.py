from django.urls import path

from random_thought import views

app_name = 'random_thought'

urlpatterns = [
    path('thought/', views.thought, name='thought'),
    path('create/', views.create_thought, name='create_thought'),
    path('list/', views.list_view, name='list_view'),
    path('<int:pk>/', views.thought_detail, name='thought_detail')
]