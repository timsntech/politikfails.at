from django.contrib import admin
from .models import Snippet, Politician, Category, Party 
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Politician)
admin.site.register(Category)
admin.site.register(Party)