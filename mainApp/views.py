from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment, Profile
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

    def post(self, request, *args, **kwargs):
        content_posts = Post.objects.all().order_by("-created")
        comment_posts = Post.objects.all()
        form = Post_Entry(request.POST)
        comment_form = Comment_Entry(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = comment_posts

        # comments = Comment.objects.filter(post=comment_posts).order_by("-created")

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post = form.save()

        context = {
            "content_list":content_posts,
            "form":form,
            "comments":comment_posts,
        }

        return render(request, "content_list.html", context)

class Dislikes(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        have_liked = False

        for liker in post.likes.all():
            if liker == request.user:
                have_liked = True
                break

        if have_liked:
            post.likes.remove(request.user)

        have_disliked = False

        for disliker in post.dislikes.all():
            if disliker == request.user:
                have_disliked == True
                break

        if not have_disliked:
            post.dislikes.add(request.user)
        if have_disliked:
            post.dislikes.remove(request.user)

        next_page = request.POST.get("next_page", "/")
        return HttpResponseRedirect(next_page)

class Likes(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        have_disliked = False

        for disliker in post.dislikes.all():
            if disliker == request.user:
                have_disliked == True
                break

        if have_disliked:
            post.likes.remove(request.user)

        have_liked = False

        for liker in post.likes.all():
            if liker == request.user:
                have_liked = True
                break

        if not have_liked:
            post.likes.add(request.user)
        if have_liked:
            post.likes.remove(request.user)

        next_page = request.POST.get("next_page", "/")
        return HttpResponseRedirect(next_page)


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by("-created")
        followers = profile.followers.all()
        followers_count = len(followers)

        if followers_count == 0:
            is_a_follower = False

        for follower in followers:
            if follower == request.user:
                is_a_follower = True
                break
            else:
                is_a_follower = False

        context = {
            "user": user,
            "profile": profile,
            "posts": posts,
            "followers_count": followers_count,
            "is_a_follower": is_a_follower,
        }

        return render(request, "profile.html", context)

class addFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect("profile", pk=profile.pk)

class removeFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect("profile", pk=profile.pk)

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ["name","bio","birthday","picture"]
    template_name = "edit_profile.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("profile", kwargs={"pk":pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

class SearchUser(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("query")
        search_results = Profile.objects.filter(Q(user__username__icontains=query))

        context = {
            "search_results": search_results,
        }

        return render(request, "search.html", context)