from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Product(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR" , "DRAFT" ,
        PUBLISHED = "PB" , "PUBLISHED"
    name = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=4 , choices=Status.choices, default=Status.DRAFT)
    tag = TaggableManager()
    def __str__(self):
        return f"{self.id}"
