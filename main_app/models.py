from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone 

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    image_url = models.CharField(max_length= 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=10, default=timezone.now())


class Comment(models.Model):
    text = models.TextField(max_length=250)
    date = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, null=True)

  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meme_id': self.meme.id})