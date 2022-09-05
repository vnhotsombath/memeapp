from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    # image = models.ForeignKey(Image, on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_Delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def get_absolute_url(self):
        # return reverse('detail', kwargs={'meme_id': self.id})

class Comment(models.Model):
    comment = models.TextField(max_length=250)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme_id = models.ForeignKey(Meme, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    meme_id = models.ForeignKey(Meme, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for meme_id:{self.meme_id} @{self.url}"
