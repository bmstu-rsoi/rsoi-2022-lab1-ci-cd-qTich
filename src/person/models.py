from django.db import models


class PersonModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    work = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}: {self.name}"
