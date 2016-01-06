from django.db import models
from django.contrib.auth.models import User

class Canvas(models.Model):
    l = 200
    company = models.CharField(max_length=30)
    originalauthor = models.ForeignKey(User)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    value_propositions = models.TextField(blank=True)
    customer_segments = models.TextField(blank=True)
    partners = models.TextField(blank=True)
    relationships = models.TextField(blank=True)
    channels = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    revenue = models.TextField(blank=True)
    cost = models.TextField(blank=True)

    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='documents/%Y/%m/%d', default='/media/default-logo.png')
    products = models.TextField(blank=True)
    links = models.TextField(blank=True)


    def get_absolute_url(self):
        return "/canvas/%i/" % self.id
