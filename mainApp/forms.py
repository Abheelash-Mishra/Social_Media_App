from django import forms
from .models import Post

class Post_Entry(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Enter your thoughts!",}))


    class Meta:
        model = Post
        fields = ["body"]