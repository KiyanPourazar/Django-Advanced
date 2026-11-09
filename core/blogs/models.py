from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
