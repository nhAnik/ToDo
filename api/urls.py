from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    path('tasks/', views.taskList, name='task-list'),
    path('tasks/<int:pk>/', views.taskDetail, name='task-detail'),
]
