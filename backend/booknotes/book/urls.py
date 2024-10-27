from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<int:pk>/', views.BookAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)