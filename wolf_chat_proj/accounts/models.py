from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = CharField(max_length=20)
    password = CharField(max_length=50)
    last_login = DateTimeField(default=timezone.now)

    def get_success_url(self):
        reverse('login')

    def __str__(self):
        return self.username