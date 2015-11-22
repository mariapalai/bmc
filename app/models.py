from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='documents/%Y/%m/%d')


class Canvas(models.Model):
    l = 200
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    value_propositions = models.TextField(blank=True)
    customer_segments = models.TextField(blank=True)
    partners = models.TextField(blank=True)
    relationships = models.TextField(blank=True)
    channels = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    revenue = models.TextField(blank=True)
    cost = models.TextField(blank=True)
    originalauthor = models.ForeignKey(User)
    relatedcompany = models.OneToOneField(Company)

