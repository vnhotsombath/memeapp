from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return HttpResponse('Meme Page!')

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