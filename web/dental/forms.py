from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Home, Global, Gallery, Reservation, Service, ServiceCat, Team, Staff, Category, Contact_us, BlogPost, Comment, FAQCategory, FAQ, FAQComment
import os
from django_ckeditor_5.widgets import CKEditor5Widget

class NewBlogCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Name of blogs category')

    
    class Meta:
        model = Category
        fields = ['title', ]
        labels = {
            'title': _('Name of blog category'),
        }
        

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'short', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'short': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write about 200 characters of introductory short...'}),
            "content": CKEditor5Widget(config_name='extends')
            #attrs={"class": "django_ckeditor_5"}, config_name="comment"
        }
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'short', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'short': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write about 200 characters of introductory short...'}),
            "content": CKEditor5Widget(config_name='extends')
            #attrs={"class": "django_ckeditor_5"}, config_name="comment"
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        

        fields = ['content','parent_comment']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }



    