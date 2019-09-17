
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from betAdmin.payments.api.viewsets import AdministratorAccountViewSet

router_viewsets = DefaultRouter()
router_viewsets.register('account/administrator', AdministratorAccountViewSet, basename='administrator_account')


urlpatterns = [
    path('', include(router_viewsets.urls)),
]
