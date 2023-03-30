from rest_framework.routers import SimpleRouter
from django.urls import include, path
from .views import (APIGetToken, CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet, TitleViewSet, UsersViewSet,
                    SignUpApiView,  APILoadData)
                    

app_name = 'api'

router = SimpleRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('users', UsersViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='сategories')
router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', SignUpApiView.as_view(), name='signup'),
    path('v1/load_data/', APILoadData.as_view(), name='signup')
]
