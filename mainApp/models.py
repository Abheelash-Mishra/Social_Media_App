from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    comment_body = models.TextField()
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
