
# Create your views here. 

from django.forms import ModelForm

from django.forms import widgets

from .models import Article


class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'media_file']
        widgets = {
            'media_file': widgets.FileInput(attrs={'accept': '.pdf,video/*', 'class': 'preview'}),
        }
