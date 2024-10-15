from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    job = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=13,null=True,blank=True) 
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    shiori = models.CharField(max_length=200, null=True, blank=True)
    unvon_lavozim = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)