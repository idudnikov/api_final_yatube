from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                       PostViewSet)

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register(
    r"posts/(?P<post_id>[\d]+)/comments", CommentViewSet, basename="comments"
)
router.register("groups", GroupViewSet)
router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls.jwt")),
]
