from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.

class SocialPosts(View):
    def get(self, request, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        context = {
            "content_list": content_posts,
        }

        return render(request, "content_list.html", context)