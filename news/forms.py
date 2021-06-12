from django import forms
from .models import News, NewsComment


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('likes', 'views', 'news_instance')


class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('likes', 'views', 'news_instance')


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        exclude = ('reader', 'news', 'comment_instance')


