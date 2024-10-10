from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
