from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# --------------------------
# Post ViewSet
# --------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Show posts from the current user + users they follow
        """
        user = self.request.user
        following_users = user.following.all()  # ✅ get all followed users
        return Post.objects.filter(author__in=following_users).order_by("-created_at") | Post.objects.filter(author=user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --------------------------
# Comment ViewSet
# --------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

