from django.db import models


# Create your models here.
class Subject(models.Model):
    query_string = models.CharField(max_length=13, primary_key=True)
    request_time = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=1000)

    def __str__(self):
        return self.query_string
