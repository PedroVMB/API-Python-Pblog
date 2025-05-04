from rest_framework import serializers
from pblog import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
