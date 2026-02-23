from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm


class HomePageView(ListView):
    model = Article
    template_name = "home.html"


class DetailPageView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    form_class = ArticleForm
    success_url = reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.is_superuser

class ArticleEditView(UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body", "publish_date"]
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser

class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser
