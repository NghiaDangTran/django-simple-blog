from pyexpat import model
from turtle import title
from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100000)
    # id=
    created_At=models.DateTimeField(default=datetime.now,blank=True)