from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            b = Book.objects.get(pk=pk)
            serializer = BookSerializer(b)
        else:
            b = Book.objects.all()
            serializer = BookSerializer(b, many=True)
        return Response({'get' : serializer.data})
    
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
        