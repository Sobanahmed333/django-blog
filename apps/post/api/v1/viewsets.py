from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.post.api.v1.serializers import PostSerializer
from apps.post.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )