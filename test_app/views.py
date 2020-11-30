from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "head"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user)


class UpvoteAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["patch"]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.upvotes += 1
        instance.save()
        return Response(serializer.data)
