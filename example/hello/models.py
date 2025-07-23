from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    mappls_pin = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
