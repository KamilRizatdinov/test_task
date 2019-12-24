import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Subject(models.Model):
    inn = models.CharField(max_length=10, primary_key=True)
    ogrn = models.CharField(max_length=13)
    request_time = models.DateTimeField(auto_now_add=True)
    registration_date = models.CharField(max_length=50)
    name_ex = models.TextField()

    def requested_recently(self):
        return self.request_time >= timezone.now() - datetime.timedelta(minutes=5)

    def to_dict(self):
        return Subject.objects.filter(pk=self.pk).values().first()

    def __str__(self):
        return self.name_ex


class Query(models.Model):
    query_string = models.CharField(max_length=13, primary_key=True)
    result = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.result.name_ex
