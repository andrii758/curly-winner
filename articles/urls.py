from django.urls import path

from .views import HomePageView, DetailPageView, ArticleCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/<int:pk>/", DetailPageView.as_view(), name="article_detail"),
    path("article/create/", ArticleCreateView.as_view(), name="article_create"),
]
