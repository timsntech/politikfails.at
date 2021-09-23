from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

CATEGORY_LEVELS = (
        ('Bestechlichkeit', 'Bestechlichkeit'),
        ('Antisemitismus', 'Antisemitismus'),
        ('Amtsmissbrauch', 'Amtsmissbrauch'),
        ('Falschaussage', 'Falschaussage'),
        ('Gesetzwidrigkeit', 'Gesetzwidrigkeit'),
        ('Verfassungswidrigkeit', 'Verfassungswidrigkeit'),
        ('Unethisches Handeln', 'Unethisches Handeln'),
        ('Unfähigkeit', 'Unfähigkeit'),
    )

PARTEIEN = (
        ('ÖVP/Liste Kurz', 'ÖVP/Liste Kurz'),
        ('SPÖ', 'SPÖ'),
        ('Bündnis90/Grüne', 'Bündnis90/Grüne'),
        ('Neos', 'Neos'),
        ('FPÖ', 'FPÖ'),
    )


# define politician model
class Politiker(models.Model):
    name = models.CharField(max_length=30)
    partei = models.CharField(choices=PARTEIEN, max_length=20)
    image = models.ImageField(upload_to ='uploads/politiker', blank=True)

    def __str__(self):
        return self.name


# define snippet model
class Snippet(models.Model):

    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    category = MultiSelectField(choices=CATEGORY_LEVELS, max_length=40)
    partei = MultiSelectField(choices=PARTEIEN, max_length=40)
    politiker = models.ManyToManyField(Politiker)
    quellen = models.JSONField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to ='uploads/snippets', blank=True)
    

    def __str_(self):
        return "Snippet for {}".format(self.name)


