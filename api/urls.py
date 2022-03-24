from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from .views import CommentViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", CommentViewSet, basename="post-comments")


urlpatterns = [url(r"^", include(router.urls)), url(r"^", include(posts_router.urls))]
