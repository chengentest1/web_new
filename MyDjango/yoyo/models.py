from django.db import models

# Create your models here.


class PeronInfo(models.Model):
    '''个人信息'''

    name=models.CharField(max_length=30,null=True,blank=True,default='默认值',verbose_name="姓名")
    age=models.IntegerField(null=True,blank=True,verbose_name='年龄')
    qq=models.CharField(max_length=30,blank=True,null=True,verbose_name='QQ')

    def __str__(self):
        return self.__doc__+":"+self.name

    class Meta:
        verbose_name_plural="个人信息表"

class chengji(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    no=models.BigIntegerField(default=0)
    create_time=models.DateTimeField(auto_now=True)
    updata_time=models.DateTimeField(auto_now=True)
    text=models.TextField(null=True,blank=True)