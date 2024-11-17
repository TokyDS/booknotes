from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
class LibraryView(TemplateView):
    template_name = 'library.html'
    
class ProfileView(TemplateView):
    template_name = 'profile.html'
    
class SignInView(TemplateView):
    template_name ='signIn.html'

class SignUpView(TemplateView):
    template_name ='signUp.html'
    
class ConspectView(TemplateView):
    template_name ='conspect.html'

class ReaderView(TemplateView):
    template_name ='reader.html'
    
class CalendarView(TemplateView):
    template_name ='calendar.html'