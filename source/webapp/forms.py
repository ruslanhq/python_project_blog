from django import forms
from django.forms import widgets

from webapp.models import Article


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    author = forms.CharField(max_length=40, required=True, label='Author')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea)


class CommentForm(forms.Form):
    article = forms.ModelChoiceField(queryset=Article.objects.all().order_by('-created_at'), required=True,
                                     label='Article', empty_label=None)
    author = forms.CharField(max_length=40, required=False, label='Author', initial='Аноним')
    text = forms.CharField(max_length=400, required=True, label='Text',
                           widget=widgets.Textarea)



