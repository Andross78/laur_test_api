from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=32)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    upvotes = models.IntegerField(default=0, null=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
