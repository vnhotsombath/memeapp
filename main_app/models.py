from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    image_url = models.CharField(max_length= 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField(max_length=250)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme_id = models.ForeignKey(Meme, on_delete=models.CASCADE)


