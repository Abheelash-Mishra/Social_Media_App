from django.urls import path
from .views import SocialPosts

urlpatterns = [
    path("", SocialPosts.as_view(), name="content_list"),
]