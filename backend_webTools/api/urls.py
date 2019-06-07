# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('Report/', views.ListReport.as_view()),
    path('Report/<int:pk>/', views.DetailReport.as_view()),
    path('Interview/', views.ListInterview.as_view()),
    path('Interview/<int:pk>/', views.DetailInterview.as_view()),
]

