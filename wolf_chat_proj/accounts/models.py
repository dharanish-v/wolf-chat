from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    username = CharField(max_length=20)
    password = CharField(max_length=50)
    
