from django.db import models
from multiselectfield import MultiSelectField
import uuid


# define model for category
class Category(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to ='uploads/category', blank=True)

    def __str__(self):
        return self.name


# define model for political party
class Party(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to ='uploads/parties', blank=True)

    def __str__(self):
        return self.name


# define politician model
class Politician(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=30)
    party = models.ForeignKey(Party, related_name='politicians', on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/politicians', blank=True)

    def __str__(self):
        return self.name


# define snippet model
class Snippet(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category)
    parties = models.ManyToManyField(Party)
    politicians = models.ManyToManyField(Politician)
    sources = models.JSONField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to ='uploads/snippets', blank=True)
    image_credits = models.CharField(max_length=3000)
    
    def __str__(self):
        return 'Snippet: ' + self.name

