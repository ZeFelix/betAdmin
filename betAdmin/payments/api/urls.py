
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from betAdmin.payments.api.viewsets import AdministratorAccountViewSet, PlanViewSet

router_viewsets = DefaultRouter()
router_viewsets.register('accounts/administrator', AdministratorAccountViewSet, basename='administrator_account')
router_viewsets.register('accounts/plans', PlanViewSet, basename='administrator_account')


urlpatterns = [
    path('', include(router_viewsets.urls)),
]
