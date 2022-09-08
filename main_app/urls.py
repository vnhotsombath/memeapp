from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/create', views.create_meme, name='create_meme'),
    path('memes/new', views.new_meme, name='new_meme'),
    path('memes/', views.memes_index, name='memes'),
    path('memes/intro', views.intro, name='intro'),
    path('memes/<int:meme_id>/', views.meme_detail, name='detail'),
    path('memes/<int:meme_id>/add_comment/', views.add_comment, name='add_comment'),
    path('memes/<int:pk>/delete', views.MemeDelete.as_view(), name='meme_delete'),
    path('memes/logout', views.logout_page, name='logout_page'),

    ]