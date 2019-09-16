
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from betAdmin.accounts.api.viewsets import SimpleProfileViewSet

router_viewsets = DefaultRouter()
router_viewsets.register(r'profiles/simple', SimpleProfileViewSet, basename='simple_profile')

from betAdmin.accounts.api.apiviews import UserAPIView


urlpatterns = [
    path('', include(router_viewsets.urls)),
    path('logout', UserAPIView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
