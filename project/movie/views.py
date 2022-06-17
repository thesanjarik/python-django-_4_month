from django.shortcuts import render
from movie.models import Movie
# Create your views here.



def director_list_view(request):
    directors = Movie.objects.all()     # QuerySet
    context = {
        'director_list': directors
    }
    print(directors)
    return render(request, 'director.html', context=context)


def movie_list_view(request):
    movies = Movie.objects.all()     # QuerySet
    context = {
        'movie_list': movies
    }
    print(movies)
    return render(request, 'movie.html', context=context)


def review_list_view(request):
    reviews = Movie.objects.all()     # QuerySet
    context = {
        'review_list': reviews
    }
    print(reviews)
    return render(request, 'review.html', context=context)


def director_detail_view(request, id):
    directors = Movie.objects.get(id=id)
    return render(request, 'director_detail.html', context={'director_detail': directors})


def movie_detail_view(request, id):
    movies = Movie.objects.get(id=id)
    return render(request, 'movie_detail.html', context={'movie_detail': movies})

def review_detail_view(request, id):
    reviews = Movie.objects.get(id=id)
    return render(request, 'review_detail.html', context={'review_detail': reviews})