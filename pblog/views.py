from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle
from pblog.models import Post
from pblog.serializers import PostSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend 
from pblog.throttles import PostAnonRateThrottle

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title', 'content']
    throttle_classes = [UserRateThrottle, PostAnonRateThrottle]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
