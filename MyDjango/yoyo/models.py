from django.db import models

# Create your models here.


class PeronInfo(models.Model):

    name=models.CharField(max_length=30)
    age=models.IntegerField(null=True,blank=True)

class chengji(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()