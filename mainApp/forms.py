from django import forms
from .models import Post,Comments

class Post_Entry(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter your thoughts!", }))

    class Meta:
        model = Post
        fields = ["body"]

class Comment_Entry():
    comment_body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":3, "placeholder":"Enter your thoughts!", }))
    class Meta:
        model = Comments
        fields = ["comment_body"]