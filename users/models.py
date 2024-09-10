from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class profiles(models.Model):
    profile_id=uuid.uuid4()
    name=models.CharField(max_length=50,null=False,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    bio=models.TextField(max_length=500)
    pic=models.ImageField(default='de.jpg')
    ud=models.IntegerField(default=00)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table='userdata'



class skills(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    owner=models.ForeignKey(profiles,on_delete=models.CASCADE,null=True,blank=True)
    e_skill=models.TextField(max_length=500,null=True,blank=True)
    ult_skill=models.TextField(max_length=500,null=True,blank=True)
    role=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return str(self.owner)
    


class accounts(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    bio=models.TextField(max_length=500)
    pic=models.ImageField(default='user.jpg')

    def __str__(self):
        return str(self.name)+' Account'