from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    title=forms.CharField(
        label="Blog post  Title",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': "enter title for your post..."})
    )
                                
    content=forms.CharField(
            label="content of post ",
            widget=forms.Textarea(attrs={'placeholder': "write your blog" })

    )

    image=forms.ImageField(
        label="image of the post",
        required=False,
        widget=forms.ClearableFileInput()
    )

    category=forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="category of the post",
        initial="choose an option",
        widget=forms.Select(),  

    )

    tags=forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Select related tags",
        widget=forms.SelectMultiple( )
    )

    class Meta:
        model=BlogPost
        fields=['title','content','image','category','tags']
