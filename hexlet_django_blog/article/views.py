from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


# # Данный код актуален до 7. Представления (Views)
# def index(request):
#     tags = ['article']
#     return render(request, 'article/index.html', context={'tags': tags},)


# # 7. Представления (Views) вместо предыдущ. функции
# class IndexView(View):
#
#     def get(self, request):
#         return HttpResponse('article')


# 8. Маршрутизация
class IndexView(View):

    def get(self, request, tags, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


def article(request):
    return redirect(reverse('current_article', kwargs={'tags': 'python', 'article_id': 42}))
