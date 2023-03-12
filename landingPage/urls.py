from django.urls import path
from landingPage.views import Landing

urlpatterns = [
    path("", Landing.as_view(), name="landing"),
]