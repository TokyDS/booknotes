from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, DeleteView
from .forms import *
from api.models import *
import html

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


class LibraryView(TemplateView):
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

class BookDeleteView(DeleteView):
    model = Book
    success_url = "books"


class ProfileView(TemplateView):
    template_name = "profile.html"


class SignInView(TemplateView):
    template_name = "signIn.html"


class SignUpView(TemplateView):
    template_name = "signUp.html"


class ConspectView(TemplateView):
    template_name = "conspect.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conspects"] = Conspect.objects.all()
        context["form"] = ConspectAdd()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.method == "POST":
            form = ConspectAdd(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = ConspectAdd()

        return self.render_to_response(context)


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
