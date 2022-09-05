from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Meme, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET ='beastcoastmeme'


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  # this will handle the POST request to /accounts/signup
  # will process the form submission, add the form data to the database
  # login the user
  error_message = ''
  if request.method == 'POST':
    #This is how to create a 'user' form object
    #that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      #This will add the user to the database
      user = form.save()
      #This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
# A bad POST or GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



class MemeCreate(CreateView):
  model = Meme
  fields = ['title', 'caption',]
  success_url= '/'



def add_photo(request, meme_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, meme_id=meme_id)
    except:
      print('An error occured uploading file to S3')
  return redirect('detail', meme_id=meme_id)