from django import forms

from .models import Post, BlogClass, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'photo',)


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogClass
        fields = ('title',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
