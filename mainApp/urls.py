from django.urls import path
from .views import SocialPosts,DeletePost

urlpatterns = [
    path("", SocialPosts.as_view(), name="content_list"),
    # path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path("post/delete/<int:pk>", DeletePost.as_view(), name="delete_post"),

]