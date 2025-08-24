from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# --------------------------
# Post ViewSet
# --------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

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


# --------------------------
# Feed View (Posts from Following)
# --------------------------
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # get all users the current user is following
        following_users = request.user.following.all()

        # filter posts by authors in that following list
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

