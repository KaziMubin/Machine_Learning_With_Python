from django.db import models


# Create your models here.
class UserInfo(models.Model):

    Name = models.CharField(max_length=120)
    Age = models.IntegerField()
    Sex = models.IntegerField()
    BP = models.IntegerField()
    Cholesterol = models.IntegerField()
    Na_to_K = models.FloatField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)
    Prediction = models.CharField(max_length=20)

