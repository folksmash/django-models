from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name