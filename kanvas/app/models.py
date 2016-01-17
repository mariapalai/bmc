from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail


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
    logo = ImageField(upload_to='/media/', blank=True)
    products = models.TextField(blank=True)
    links = models.TextField(blank=True)

    def get_absolute_url(self):
        return "/canvas/%i/" % self.id

    def get_thumb(self):
        im = get_thumbnail(self.logo, '100x100', crop='center', quality=99)
        if im:
            return im.url
        else:
            return None # remember that sorl objects have url/width/height attributes