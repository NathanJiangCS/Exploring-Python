from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    #Possible Fields
    #IntegerField, DecimalField
    #CharField (requires max_length attribute)
    #TextField (unbound length)
    #EmailField, URLField (Checks that a Email and URL are valid in format)
    #FileField, ImageField
    #BooleanField
    #DateTimeField

    #Possible Attributes
    #max_length
    #null (can be true or false, meaning that null is acceptible for that field)
    #blank (can be true or false, meaning that blank space is allowed. Used in textual fields)
    #default (set the default value)
    #choices (limits the possible responses for that field)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

        
