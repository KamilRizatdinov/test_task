from django.db import models


# Create your models here.
class Subject(models.Model):
    inn = models.CharField(max_length=10, primary_key=True)
    ogrn = models.CharField(max_length=13)
    cityname = models.CharField(max_length=50)
    citytype = models.CharField(max_length=50)
    registration_date = models.CharField(max_length=50)
    name_ex = models.TextField()
    description = models.TextField()
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_ex
