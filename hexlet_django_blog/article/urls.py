from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.article),
    # path('', views.IndexView.as_view()),  # 7 Представления (Views)
    path('<str:tags>/<int:article_id>/', views.IndexView.as_view(), name='current_article'), # 8. Маршрутизация вместо предыдущ. строчки
]
