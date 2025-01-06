from django.urls import path

from booknotes import settings
from .views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # path('', views.index),
    path("", IndexView.as_view(), name="home"),
    path("books", LibraryView.as_view(), name="books"),
    path("books/<int:book_id>", BookDetailView.as_view(), name="book"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("login", views.login_view, name="login"),
    path("registration", views.register_view, name="registration"),
    path("conspect", ConspectView.as_view(), name="conspect"),
    path("notes", NotesView.as_view(), name="notes"),
    
    path("reader/<int:book_id>", ReaderView.as_view(), name="reader"),
    path("calendar", CalendarView.as_view(), name="calendar"),
    path("logout", views.logout_view, name="logout"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)