from rest_framework import fields, serializers
from .models import Snippet, Politician, Category, Party


class PoliticianSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Politician
        fields = ("id", "name", "parties", "image")
        depth = 1

class PoliticianInPartySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Politician
        fields = ("id", "name")
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("id", "name")
        depth = 1


class PartySerializer(serializers.ModelSerializer):
    
    politiker = PoliticianInPartySerializer(many=True, read_only=True)

    class Meta:
        model = Party
        fields = ("id", "name", "image", "politicians")
        depth = 1


class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = ("id", "name", "description", "image", "image_credits", "category", "parties", "sources", "date", "politicians")
        depth = 2
