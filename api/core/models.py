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

class Snippet(models.Model):

    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    category = MultiSelectField(choices=CATEGORY_LEVELS, max_length=40)
    references = models.JSONField()

    def __str_(self):
        return "Recipe for {}".format(self.name)