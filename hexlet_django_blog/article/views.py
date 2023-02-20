from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


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


# 16. Создание (CRUD)
class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been created successfully.')
            return redirect('/articles')
        messages.error(request, 'Please correct the following errors:')
        return render(request, 'articles/create.html', {'form': form})


# 17. Обновление (CRUD)
class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been updated successfully.')
            return redirect('/articles')
        messages.error(request, 'Please correct the following errors:')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


# 18. Удаление (CRUD)
class ArticleFormDestroyView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'The article has been removed successfully.')
        return redirect('/articles')
