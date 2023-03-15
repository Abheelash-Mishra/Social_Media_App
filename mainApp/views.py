from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from .forms import Post_Entry, Comment_Entry
from django.shortcuts import redirect
from django.views.generic import UpdateView, DeleteView

# Create your views here.

# class EditPost(UpdateView):
#     model = Post
#     fields = ["body"]
#     template_name =  "edit_post.html"
#
#     def get_success_url(self):
#

# def post_view(request, post_id):
#     post = Post.objects.get(id=post_id)
#     return render(request, 'content_list.html', {'post': post})
# def edit_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == 'POST':
#         post.body = request.POST.get('body')
#         post.save()
#         return redirect(post_view, post_id=post.id)
#     return render(request, 'edit_post.html', {'post': post})


class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("content_list")
class SocialPosts(View):
    def get(self, request, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        form = Post_Entry()
        comment = Comment_Entry()

        context = {
            "content_list":content_posts,
            "form":form,
            "comment":comment,
        }

        return render(request, "content_list.html", context)

    def post(self, request, post_ID, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        comment_posts = Post.objects.get(post_ID=post_ID)
        form = Post_Entry(request.POST)
        comment_form = Comment_Entry(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = comment_posts

        comments = Comment.objects.filter(post=comment_posts).order_by("-created")

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post = form.save()

        context = {
            "content_list":content_posts,
            "form":form,
            "comments":comments,
        }

        return render(request, "content_list.html", context)