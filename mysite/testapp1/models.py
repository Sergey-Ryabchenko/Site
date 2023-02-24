from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.surname} {self.name}'

# Create your models here.
