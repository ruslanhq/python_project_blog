from django import forms
from django.forms import widgets

from webapp.models import Article, Comment


class ArticleForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False, label='Tag')

    class Meta:
        model = Article
        fields = ['title', 'author', 'text']


class CommentForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['article'].queryset = Article.objects.filter(status=STATUS_ACTIVE)

    # article = forms.ModelChoiceField(queryset=Article.objects.filter(status=STATUS_ACTIVE), label='Статья')

    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


