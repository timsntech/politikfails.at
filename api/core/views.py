from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnippetSerializer, PoliticianSerializer, CategorySerializer, PartySerializer
from .models import Snippet, Politician, Party, Category

class SnippetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

class PoliticianViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PoliticianSerializer
    queryset = Politician.objects.all()

class PartyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartySerializer
    queryset = Party.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()