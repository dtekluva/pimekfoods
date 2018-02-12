from django.db import models
import time
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Customers(models.Model):
    email = models.CharField(max_length=100)
    date  = models.FloatField(default=time.time(), null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    class Meta:
        ordering = ('email',)

class Page(models.Model):
    hits  = models.IntegerField(blank=True, default = 0)
    email = models.CharField(max_length=20, blank=True, default = "notifymailer@gmail.com")

class Messages(models.Model):
    message = models.TextField(max_length=400)
    name   = models.CharField(max_length=20,blank=True)
    phone  = models.IntegerField(blank=True, null = False)
    isread    = models.BooleanField(default = False)
    isread    = models.BooleanField(default = False)
    added     = models.FloatField(default=time.time(), null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.message

    class Meta:
        ordering = ('added',)



class Product(models.Model):
    name            = models.CharField(max_length=30,unique=True)
    price           = models.IntegerField(default=0)
    details         = models.CharField(max_length=100,blank=True)
    slug            = models.SlugField(blank=True,unique=True)
    comments        = models.IntegerField(default=0)
    pub_date        = models.DateField(auto_now=True, blank=True)
    added           = models.FloatField(default=time.time(), null=True, blank=True)
    image           = models.FileField(upload_to='product-imgs/',null=True, blank=True)
    posted_by       = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null = True)
    is_top          = models.BooleanField(default = False)
    date            = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)



class UserAccount(models.Model):
    User        = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "user")
    image       = models.FileField(upload_to='profile-imgs/',null=True, blank=True)
    joined      = models.IntegerField(default=time.time(),  blank=True)

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name_plural = 'User Accounts'