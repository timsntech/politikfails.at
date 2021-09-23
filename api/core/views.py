from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnippetSerializer, PolitikerSerializer
from .models import Snippet, Politiker

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

class PolitikerViewSet(viewsets.ModelViewSet):
    serializer_class = PolitikerSerializer
    queryset = Politiker.objects.all()