from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from news.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["get"])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote()
        serializer = PostSerializer(post)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["post_pk"])
