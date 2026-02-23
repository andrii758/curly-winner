from django.urls import path

from .views import HomePageView, DetailPageView, ArticleCreateView, ArticleEditView, ArticleDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/<int:pk>/", DetailPageView.as_view(), name="article_detail"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/edit/", ArticleEditView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
