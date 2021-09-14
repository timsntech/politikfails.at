from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnippetSerializer
from .models import Snippet

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()