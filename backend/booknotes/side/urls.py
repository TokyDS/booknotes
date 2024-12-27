from django.urls import path

from booknotes import settings
from .views import *
from django.conf.urls.static import static
# from . import views
urlpatterns = [
    # path('', views.index),
    path("", IndexView.as_view(), name="home"),
    path("books", LibraryView.as_view(), name="books"),
    path("books/<int:book_id>", BookDetailView.as_view(), name="book"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("login", SignInView.as_view(), name="login"),
    path("registration", SignUpView.as_view(), name="registration"),
    path("conspect", ConspectView.as_view(), name="conspect"),
    path("reader", ReaderView.as_view(), name="reader"),
    path("calendar", CalendarView.as_view(), name="calendar"),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)