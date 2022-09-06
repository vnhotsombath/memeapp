from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/create', views.create_meme, name='create_meme'),
    path('memes/new', views.new_meme, name='new_meme'),
    path('memes/', views.memes_index, name='memes'),
    path('memes/intro', views.intro, name='intro'),

    ]