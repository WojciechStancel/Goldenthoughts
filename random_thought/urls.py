from django.urls import path

from random_thought import views

app_name = 'random_thought'

urlpatterns = [
    path('', views.thought, name='thought'),
    path('create/', views.create_thought, name='create_thought'),
    path('list/', views.list_view, name='list_view'),
    path('<int:pk>/', views.thought_detail, name='thought_detail'),
    path('update/<int:pk>/', views.update_thought, name='update_thought'),
    path('delete/<int:pk>/', views.delete_thought, name='delete_thought'),
]