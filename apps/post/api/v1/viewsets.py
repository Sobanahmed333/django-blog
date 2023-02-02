from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.post.api.v1.serializers import PostSerializer, CommentSerializer
from apps.post.models import Post, Comment


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
