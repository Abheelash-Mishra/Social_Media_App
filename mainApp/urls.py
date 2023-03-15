from django.urls import path
from .views import SocialPosts, DeletePost, ProfileView, EditProfileView, addFollower, removeFollower, Likes, Dislikes, SearchUser

urlpatterns = [
    path("", SocialPosts.as_view(), name="content_list"),
    # path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path("post/delete/<int:pk>", DeletePost.as_view(), name="delete_post"),
    path("post/<int:pk>/likes", Likes.as_view(), name="likes"),
    path("post/<int:pk>/dislikes", Dislikes.as_view(), name="dislikes"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", EditProfileView.as_view(), name="profile_edit"),
    path("profile/<int:pk>/followers/add", addFollower.as_view(), name="add_follower"),
    path("profile/<int:pk>/followers/remove", removeFollower.as_view(), name="remove_follower"),
    path("search/", SearchUser.as_view(), name="search_user")
]