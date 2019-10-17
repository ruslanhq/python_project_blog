from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import ArticleForm
from webapp.models import Article
# from .base_views import UpdateView


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    template_name = 'article/update.html'
    redirect_url = ''
    model = Article
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('article_view', kwargs={self.pk_kwargs_page: self.object.pk})


class IndexView(ListView):
    context_object_name = 'articles'
    model = Article
    template_name = 'article/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 2


class ArticleView(TemplateView):
    template_name = 'article/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_pk = kwargs.get('pk')
        context['article'] = get_object_or_404(Article, pk=article_pk)
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article/delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('index')


