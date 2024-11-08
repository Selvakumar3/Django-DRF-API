from django.urls import path
from api import views

urlpatterns = [
    path('cars/', views.carsList.as_view()),
    path('cars/<int:pk>/', views.carsdetail.as_view()),
]