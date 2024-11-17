from django.contrib import admin
from django.urls import path, include
from api.views import *
from side.views import *
# from booknotes import views
urlpatterns = [
    path('', include('side.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
] 
