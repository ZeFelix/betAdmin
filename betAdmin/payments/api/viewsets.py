from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from betAdmin.payments.api.serializers import AdministratorAccountSerializer
from betAdmin.payments.models import AdministratorAccount


class AdministratorAccountViewSet(ReadOnlyModelViewSet):
    serializer_class = AdministratorAccountSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return AdministratorAccount.objects.filter(is_active=True)

