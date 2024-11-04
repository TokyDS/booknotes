from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from .filters import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['id', 'title', 'author']
    ordering = ['id']
    
    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        b = get_object_or_404(queryset, pk=pk)
        book_serializer = BookSerializer(b)
        n = Note.objects.filter(book=b)
        note_serializer = NoteSerializer(n, many=True)
        data = {"book": book_serializer.data, 
                "notes": note_serializer.data}
        return Response({'get' : data})

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        a = get_object_or_404(queryset, pk=pk)
        author_serializer = AuthorSerializer(a)
        b = Book.objects.filter(author=a)
        book_serializer = BookSerializer(b, many=True)
        data = {"author": author_serializer.data, 
                 "books": book_serializer.data}
        return Response({'get' : data})
    
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = NoteFilter
    ordering_fields = ['id', 'title', 'tag']
    ordering = ['id']

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    