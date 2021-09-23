from rest_framework import fields, serializers
from .models import Snippet, Politiker
from .models import CATEGORY_LEVELS, PARTEIEN



class PolitikerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Politiker
        fields = ("id", "name", "partei", "image")


class SnippetSerializer(serializers.ModelSerializer):
    category = fields.MultipleChoiceField(choices=CATEGORY_LEVELS)
    partei = fields.MultipleChoiceField(choices=PARTEIEN)
    #politiker = PolitikerSerializer(many=True)
    
    class Meta:
        model = Snippet
        fields = ("id", "name", "description", "category", "partei", "quellen", "date", "politiker")
        depth = 1
