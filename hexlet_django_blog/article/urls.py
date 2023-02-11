from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view()),  # 7 Представления (Views) вместо предыдущ. строчки
]
