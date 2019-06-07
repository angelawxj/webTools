# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.ListReport.as_view()),
    path('report/<int:pk>/', views.DetailReport.as_view()),
    path('interview/', views.ListInterview.as_view()),
    path('interview/<int:pk>/', views.DetailInterview.as_view()),
]

