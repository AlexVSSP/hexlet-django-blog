from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

from hexlet_django_blog.article.models import Article


# # Данный код актуален до 7. Представления (Views)
# def index(request):
#     tags = ['article']
#     return render(request, 'article/index.html', context={'tags': tags},)


# # 7. Представления (Views) вместо предыдущ. функции
# class IndexView(View):
#
#     def get(self, request):
#         return HttpResponse('article')


# 8. Маршрутизация закомитчена из-за 13. Список (Article)
# class IndexView(View):
#
#     def get(self, request, tags, article_id):
#         return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
#
#
# def article(request):
#     return redirect(reverse('current_article', kwargs={'tags': 'python', 'article_id': 42}))


# 13. Список (CRUD)
class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


# 14. Просмотр (CRUD)
class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })
