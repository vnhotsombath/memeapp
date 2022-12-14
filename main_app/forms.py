from django.forms import ModelForm
from .models import Meme, Comment

class MemeForm(ModelForm):
	class Meta:
		model = Meme 
		fields = ['title', 'caption', 'date', 'image_url']

class CommentForm(ModelForm):
	class Meta:
		model = Comment 
		fields = ['text']