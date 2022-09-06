from django.forms import ModelForm
from .models import Meme

class MemeForm(ModelForm):
	class Meta:
		model = Meme 
		fields = ['title', 'caption', 'image_url']