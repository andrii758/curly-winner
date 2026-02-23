from django import forms 

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'publish_date']
        widgets = {
                # widget brings up browser's default calendar
                'publish_date': forms.DateTimeInput(
                    attrs={'type': 'datetime-local', 'class': 'form-control'},
                    format='%Y-%m-%dT%H:%M'
                ),
        }


