from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/create/', views.MemeCreate.as_view(), name='memes_create'),
    path('memes/<int:meme_id>/add_photo/', views.add_photo, name='add_photo'),
    path('memes/', views.memes_index, name='memes'),
    ]