from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, DeleteView
from .forms import *
from api.models import *
import html
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all().order_by("-pk")[:3]
        context["form"] = BookAdd()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.method == "POST":
            form = BookAdd(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        else:
            form = BookAdd()
        return HttpResponseRedirect('/')

class LibraryView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "library.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_updated"] = Book.objects.all().order_by("-pk")
        context["books"] = Book.objects.all()
        context["form"] = BookAdd()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.method == "POST":
            form = BookAdd(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form = BookAdd()
        return HttpResponseRedirect('books')



class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = "book_id"
    template_name = "book.html"
    context_object_name = "book"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        context["conspects"] = Conspect.objects.filter(book=book)
        context["notes"] = Note.objects.filter(book=book)
        return context

class BookDeleteView(DeleteView):
    model = Book
    success_url = "books"


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "profile.html"


class SignInView(TemplateView):
    template_name = "signIn.html"
    


class SignUpView(TemplateView):
    template_name = "signUp.html"


class ConspectView(TemplateView):
    template_name = "conspect.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conspects = Conspect.objects.all()
        context["conspects"] = conspects
        context["form"] = ConspectAdd()
        context["books"] = Book.objects.filter(conspect__in=conspects).distinct()
        return context


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.method == "POST":
            form = ConspectAdd(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = ConspectAdd()

        return HttpResponseRedirect('/conspect')

class NotesView(TemplateView):
    template_name = "notes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = Note.objects.all()
        context["notes"] = notes
        context["form"] = ConspectAdd()
        return context


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.method == "POST":
            form = NoteAdd(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = NoteAdd()

        return HttpResponseRedirect('/notes')


class ReaderView(TemplateView):
    model = Book
    template_name = "reader.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(pk=self.kwargs['book_id'])
        with book.book.open('r') as f:
            context["book"] = book
            context["text"] = html.escape(''.join(f.readlines()))
        return context


class CalendarView(TemplateView):
    template_name = "calendar.html"

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login successful")
                return redirect('home')
            else:
                print("Login failed")
    else:
        form = LoginForm()
    return render(request, 'signIn.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signUp.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')