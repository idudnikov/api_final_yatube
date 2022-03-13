from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register(
    r"posts/(?P<post_id>[\d]+)/comments", CommentViewSet, basename="comments"
)
router.register("groups", GroupViewSet)

urlpatterns = [
    path("api-token-auth/", obtain_auth_token),
    path("", include(router.urls)),
]
