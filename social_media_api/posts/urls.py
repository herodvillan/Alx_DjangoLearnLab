from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostFeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', PostFeedView.as_view(), name='post-feed'),
    path("like/<int:post_id>/", LikePostView.as_view(), name="like-post"),
    path("unlike/<int:post_id>/", UnlikePostView.as_view(), name="unlike-post"),
    path("<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
    path("<int:post_id>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]

