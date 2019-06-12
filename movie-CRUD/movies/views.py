from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Movie
# Create your views here.

@require_GET
def index(request):

    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):

    if request.method =='GET':
        return render(request, 'movies/new.html')
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score= request.POST.get('score')
        poster_url= request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie(title=title, title_origin=title_origin, vote_count=vote_count,
                      open_date=open_date, genre=genre,score=score,poster_url=poster_url,description=description)
        movie.save()
        return redirect('movies:index')


@require_GET
def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def edit(request, id):

    movie = get_object_or_404(Movie, id=id)

    if request.method=='GET':
        context = {'movie': movie}
        return render(request, 'movies/edit.html', context)

    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')


        movie.title = title
        movie.title_origin= title_origin
        movie.vote_count = vote_count
        movie.open_date = open_date
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description

        movie.save()
        return redirect('movies:detail', id)


def delete(request, id):
    pass
