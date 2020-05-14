from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-task/<int:pk>/', views.updateTask, name='update'),
    path('delete-task/<int:pk>/', views.deleteTask, name='delete'),
]
