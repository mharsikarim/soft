
from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.contrib.auth.models import User
import datetime
import os
from datetime import datetime

from account.models import User


def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%h:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join("uploads/",filename)

class Category(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    status=models.BooleanField(default=False,help_text='0=default ,1=Hidden')
    class Meta:
        ordering=['-name']
    def __str__(self):
        return self.name
class Services(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField()
    category= ForeignKey(Category,related_name='categorie',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    date_added=models.DateField(auto_now=True)
    class Meta:
        ordering=['-date_added']
    def __str__(self):
        return self.title
class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(Services,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateField(auto_now_add=True)

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Services,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)



class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    def __str__(self):
        return self.room