from django.urls import path
from . import views

urlpatterns = [
    path('',views.movie_view,name='movie'),
    path('list/',views.movie_list,name='list'),
    path('add/',views.add_movie,name='add')
]