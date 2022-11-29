from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(
    'posts',
    PostViewSet
)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename='comments'
)
router.register(
    'groups',
    GroupViewSet
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
