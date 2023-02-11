from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def index(request):
#     tags = ['article']
#     return render(request, 'article/index.html', context={'tags': tags},)


# 7 Представления (Views) вместо предыдущ. функции
class IndexView(View):

    def get(self, request):
        return HttpResponse('article')
