from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'notes', views.NoteViewSet, basename='note')
router.register(r'tags', views.TagViewSet, basename='tag')
urlpatterns = router.urls
