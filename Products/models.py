from django.db import models
from s3direct.fields import S3DirectField

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=30)
    date_published = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.FileField(upload_to='media/') 

def __str__(self):
    return self.name