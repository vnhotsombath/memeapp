from django.contrib import admin
from .models import Meme, Comment, Image

# Register your models here.
admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Image)