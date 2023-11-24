from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework import viewsets
from django.shortcuts import render
from .models import book
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    