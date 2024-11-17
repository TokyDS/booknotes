from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'notes', views.NoteViewSet, basename='note')
router.register(r'tags', views.TagViewSet, basename='tag')

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  
] + router.urls

