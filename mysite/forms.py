from django import forms
from .models import Article, Comment, Report
from crispy_forms.helper import FormHelper


class Form(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('topic', 'title', 'body',)

        widgets = {
            'topic': forms.Select(attrs={'class': 'form-control', "style": "width: 15%"}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Comment
        fields = ('name', 'body',)
        widgets = {
          'name': forms.Textarea(attrs={'rows':1, 'cols':30, 'placeholder': 'Your name'}),
          'body': forms.Textarea(attrs={'rows':2, 'cols':60, 'placeholder':'Add a comment', "style": "margin-top:-30px"}),
        }


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('title', 'email',)

