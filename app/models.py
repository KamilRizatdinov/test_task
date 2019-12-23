from django.db import models


# Create your models here.
class Subject(models.Model):
    query_string = models.CharField(max_length=100)
    query_type = models.CharField(max_length=5)
    result = models.CharField(max_length=1000)

    def __str__(self):
        return self.query_string
