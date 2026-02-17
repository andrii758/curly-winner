from django.views.generic import ListView, DetailView

from .models import Article


class HomePageView(ListView):
    model = Article
    template_name = "home.html"


class DetailPageView(DetailView):
    model = Article
    template_name = "article_detail.html"
