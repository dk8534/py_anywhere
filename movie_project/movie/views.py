from django.shortcuts import render
from .models import movie
from .forms import AddMoviePage
# Create your views here.

def movie_view(request):
    return render(request,'movie.html')
def movie_list(request):
    movie_list = movie.objects.all()
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'movie_list.html', context)
def add_movie(request):
    movie = AddMoviePage()
    submit = False
    if request.method == 'POST':
        movie = AddMoviePage(request.POST)
        if movie.is_valid():
            movie.save()
            submit = True
    context = {'form':movie,
               'submit':submit}        
    return render(request,'movie_add.html',context)

