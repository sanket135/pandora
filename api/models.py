import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True, unique=True)
    objects = models.Manager()

class Vegetable(models.Model):
    name = models.CharField(max_length=20, blank=True)
    objects = models.Manager()

class favouriteFood(models.Model):
    name = models.CharField(max_length=30, blank=True)
    objects = models.Manager()

class Fruit(models.Model):
    name = models.CharField(max_length=20, blank=True)
    objects = models.Manager()

class Company(models.Model):
    objects = models.Manager()
    index = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=50, blank=True)


    def __str__(self):
        # return "{}".format(self.id)
        return u'%s %s' % (self.company, self.index)


class User(AbstractUser):
    _id = models.CharField(max_length=70, blank=True)
    index = models.IntegerField(null=True, blank=True)
    guid = models.CharField(max_length=70, blank=True)
    has_died = models.BooleanField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    eyeColor = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=90, blank= False)
    gender = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=120, blank=True)
    about = models.TextField(max_length=500, blank=True)
    registered = models.CharField(max_length=30, blank=True)
    greeting = models.CharField(max_length=120, blank=True)
    friends = models.ManyToManyField("self", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    fruit = models.ManyToManyField(Fruit, blank=True)
    company = models.ManyToManyField(Company, blank=True, related_name="employees")
    favouriteFood = models.ManyToManyField(favouriteFood, blank=True)



