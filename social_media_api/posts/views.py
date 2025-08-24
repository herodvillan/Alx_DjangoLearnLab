from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like
from notifications.models import Notification


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        # Prevent duplicate likes
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)

        # ✅ Create a notification for the post author
        if post.author != request.user:  # don’t notify yourself
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )

        return Response({"detail": "Post liked successfully."},
                        status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You haven’t liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked successfully."},
                        status=status.HTTP_200_OK)


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

