from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('article')


def index(request):
    tags = ['article']
    return render(request, 'article/index.html', context={'tags': tags},)
