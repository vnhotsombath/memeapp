from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login
from .models import Meme, Comment
from .forms import MemeForm, CommentForm
import datetime
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET ='beastcoastmemer'


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
      return render(request, 'meme/intro.html')
    else:
      error_message = 'Invalid sign up - try again'
# A bad POST or GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def new_meme(request):
  form = MemeForm(request.POST)
  if form.is_valid():
        # were creating an object to save to the database, but don't save yet, because
        # we need to add meme_id
        new_meme = form.save(commit=False)
        new_meme.meme_id = meme_id
        new_meme.save() # saves the meme to the database!
    # import redirect at the top
  return render(request, 'new_meme.html')


@login_required
def create_meme(request):
 
  photo_file = request.FILES.get('photo-file', None)
  print( request.POST.get('caption'), "<<<<<<<<<<<<<<<<<<<<<AWS CAPTION")
  print( request.POST.get('title'), "<<<<<<<<<<<<<<<<<<<<<AWS CAPTION")
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"

      print(url, "<<<<<<<<<<<<<<<<<<<<<AWS URL")
      # print(request.user, "<--REQ.USER", request.title, "<-- REQ.TITLE", request.caption, "<---REQ.CAPTION")
      print('HELLLLLLOOOOOOOOOOO')
      print(request.user, 'request.user here')
      Meme.objects.create(image_url=str(url), user=request.user, title=request.POST.get('title'), caption=request.POST.get('caption'),)

    except:
      print('An error occured uploading file to S3')

  return redirect('/memes')

def memes_index(request):
  memes = Meme.objects.all()
  return render(request, 'meme/index.html', { 'memes': memes})

@login_required
def intro(request):
  return render(request, 'meme/intro.html')

@login_required 
def meme_detail(request, meme_id):
  meme = Meme.objects.get(id=meme_id)
  comment_form = CommentForm()
  return render(request,'meme/detail.html', {'meme': meme, 'comment_form': comment_form})

@login_required
def add_comment(request, meme_id):
    form = CommentForm(request.POST)
    current_datetime = datetime.datetime.now()
    print(current_datetime, '<--------DATE')
   #print(request.POST.get('comment'), '<--------COMMENT')
    # print(request.user, '<--------USER')
    # print(meme_id, '<----------MEMEID')
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.meme_id = meme_id
        new_comment.user_id=request.user.id
        #Comment.objects.create(user=request.user, meme_id=meme_id, comment=request.POST.get('comment'), date=current_datetime)
        new_comment.save()
      
    return redirect('detail', meme_id=meme_id)

class MemeDelete(DeleteView):
    model = Meme 
    success_url = '/memes/'

def logout_page(request):
  return render(request, 'registration/logout.html')