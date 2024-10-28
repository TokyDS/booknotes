from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'notes', views.NoteViewSet, basename='note')
urlpatterns = router.urls


# urlpatterns = [
#     path('books/', views.BookAPIView.as_view()),
#     path('books/<int:pk>/', views.BookAPIView.as_view()),
#     path('authors/', views.AuthorAPIView.as_view()),
#     path('authors/<int:pk>/', views.AuthorAPIView.as_view()),
#     path('notes/', views.NoteAPIView.as_view()),
#     path('notes/<int:pk>/', views.NoteAPIView.as_view()),
    # path('categories/', views.CategoryAPIView.as_view()),
    # path('categories/<int:pk>/', views.CategoryAPIView.as_view()),
    # path('tags/', views.TagAPIView.as_view()),
    # path('tags/<int:pk>/', views.TagAPIView.as_view()),
    # path('genres/', views.GenreAPIView.as_view()),
    # path('genres/<int:pk>/', views.GenreAPIView.as_view()),
    # path('publishers/', views.PublisherAPIView.as_view()),
    # path('publishers/<int:pk>/', views.PublisherAPIView.as_view()),
# ]
