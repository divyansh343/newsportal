from django.db import models
from django.db.models.aggregates import Min
from tinymce.models import HTMLField 
  
# Create your models here.

class Post(models.Model):
    sno = models.AutoField
    title = models.CharField(max_length=800)
    description = models.CharField(max_length=800, default="")
    author = models.CharField(max_length=80)
    slug = models.SlugField()
    content = HTMLField()
    image = models.ImageField(upload_to='img/images', default="")


    def __str__(self):
        return self.title + " by " + self.author