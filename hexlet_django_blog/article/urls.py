from django.urls import path

# from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView

urlpatterns = [
    # path('', views.article),  # Закомитчено из-за 13. Список (CRUD)
    # path('', views.IndexView.as_view()),  # 7 Представления (Views)
    path('<str:tags>/<int:article_id>/', IndexView.as_view(), name='current_article'), # 8. Маршрутизация вместо предыдущ. строчки
    path('', IndexView.as_view()),  # 13. Список (CRUD)
    path('<int:id>/', ArticleView.as_view(), name='articles_detail'),  # 14. Просмотр (CRUD)
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),  # 16. Создание (CRUD)
]
