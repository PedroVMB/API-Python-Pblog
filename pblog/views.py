from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.throttling import UserRateThrottle
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from pblog.models import Post, Image
from pblog.serializers import PostSerializer, UserSerializer, ImageSerializer
from pblog.throttles import PostAnonRateThrottle

from django.contrib.auth.models import User 

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title', 'content']
    throttle_classes = [UserRateThrottle, PostAnonRateThrottle]
    
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('id') 
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
