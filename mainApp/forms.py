from django import forms
from .models import Post, Comment

class Post_Entry(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter your thoughts!", }))

    class Meta:
        model = Post
        fields = ["body"]

class Comment_Entry(forms.ModelForm):
    comment_body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 1, "placeholder": "Enter your comment", }))

    class Meta:
        model = Comment
        fields = ["comment_body"]