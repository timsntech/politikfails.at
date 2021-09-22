from rest_framework import fields, serializers
from .models import Snippet
from .models import CATEGORY_LEVELS

class SnippetSerializer(serializers.ModelSerializer):
    category = fields.MultipleChoiceField(choices=CATEGORY_LEVELS)
    
    class Meta:
        model = Snippet
        fields = ("id", "name", "description", "category", "references")