from django.shortcuts import render
from django.http import HttpResponse

# dummay data 

posts = [
    {
        'author': 'Nimesh',
        'title' : 'Blog Post 1',
        'content' : 'First post contents',
        'date_posted': 'July 21, 2024'
    },
    {
        'author': 'Abhishek',
        'title' : 'Blog Post 2',
        'content' : 'Second post contents',
        'date_posted': 'July 25, 2024'
    }
]


# home page of blog website
def home(request):
    context = {
        'posts': posts
    }

    # return HttpResponse('<h1>Blog Home </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request ,'blog/about.html', {'title':'About'})   