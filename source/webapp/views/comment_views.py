from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Comment


class CommentIndexView(ListView):
    context_object_name = 'comment'
    template_name = 'comment/comment_index.html'
    model = Comment
    ordering = ['-created_at']


class CommentCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, 'comment/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                article=form.cleaned_data['article']
            )
            return redirect('comment_index_view')
        else:
            return render(request, 'comment/create.html', context={'form': form})


class CommentUpdateView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data={
            'title': comment.article,
            'author': comment.author,
            'text': comment.text
        })
        return render(request, 'comment/update.html', context={'form': form, 'comment': comment})

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment.article = form.cleaned_data['article']
            comment.author = form.cleaned_data['author']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('comment_index_view')
        else:
            return render(request, 'article/update.html', context={'form': form, 'comment': comment})


class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})
