from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Имя')
    email = forms.EmailField(label='E-mail', initial='lifeh2400@gmail.com')
    to = forms.EmailField(label='Кому(адрес)')
    comments = forms.CharField(required=False,
                               widget=forms.Textarea,
                               label='Комментарий к записи')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField(label='Введите текст')

