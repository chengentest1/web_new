from django.db import models

# Create your models here.


class PeronInfo(models.Model):

    name=models.CharField(max_length=30,null=True,blank=True,default='默认值')
    age=models.IntegerField(null=True,blank=True)
    qq=models.CharField(max_length=30,blank=True,null=True)

class chengji(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    no=models.BigIntegerField(default=0)
    create_time=models.DateTimeField(auto_now=True)
    updata_time=models.DateTimeField(auto_now=True)
    text=models.TextField(null=True,blank=True)