from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.

class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            b = Book.objects.get(pk=pk)
            book_serializer = BookSerializer(b)
            n = Note.objects.filter(book=b)
            note_serializer = NoteSerializer(n, many=True)
            data = {"book": book_serializer.data, 
                    "notes": note_serializer.data}
        else:
            b = Book.objects.all()
            serializer = BookSerializer(b, many=True)
            data = serializer.data
        return Response({'get' : data})
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'post' : serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Book.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Book.objects.get(pk=pk)
            instance.delete()

        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})

class AuthorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            a = Author.objects.get(pk=pk)
            author_serializer = AuthorSerializer(a)
            b = Book.objects.filter(author=a)
            book_serializer = BookSerializer(b, many=True)
            data = {'author': author_serializer.data,
                    'books':  book_serializer.data}
        else:
            a = Author.objects.all()
            serializer = AuthorSerializer(a, many=True)
            data = serializer.data
        return Response({'get' : data})
    
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'post' : serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = AuthorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Author.objects.get(pk=pk)
            instance.delete()

        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})
    
class NoteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            n = Note.objects.get(pk=pk)
            serializer = NoteSerializer(n)
        else:
            n = Note.objects.all()
            serializer = NoteSerializer(n, many=True)
        return Response({'get' : serializer.data})
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'post' : serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Note.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = NoteSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Note.objects.get(pk=pk)
            instance.delete()

        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})