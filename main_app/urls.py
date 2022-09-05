from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/create/', views.MemeCreate.as_view(), name='memes_create'),
]