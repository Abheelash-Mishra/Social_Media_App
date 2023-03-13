from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import Post_Entry

# Create your views here.

class SocialPosts(View):
    def get(self, request, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        form = Post_Entry()

        context = {
            "content_list": content_posts,
            "form": form,
        }

        return render(request, "content_list.html", context)

    def post(self, request, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        form = Post_Entry(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post = form.save()

        context = {
            "content_list":content_posts,
            "form":form,
        }

        return render(request, "content_list.html", context)