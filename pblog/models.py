from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    description = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.description

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ForeignKey(Image, related_name='posts', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
