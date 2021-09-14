from django.db import models
# Create your models here.

class Snippet(models.Model):
    CATEGORY_LEVELS = (
        ('Korruption', 'Korruption'),
        ('Verleumdung', 'Verleumdung'),
        ('Betrug', 'Betrug'),
    )
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    category = models.CharField(choices=CATEGORY_LEVELS, max_length=20)
    references = models.JSONField()

    def __str_(self):
        return "Recipe for {}".format(self.name)