from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from betAdmin.payments.api.serializers import AdministratorAccountSerializer, PlanSerializer
from betAdmin.payments.models import AdministratorAccount, Plan


class AdministratorAccountViewSet(ReadOnlyModelViewSet):
    serializer_class = AdministratorAccountSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return AdministratorAccount.objects.filter(is_active=True)


class PlanViewSet(ReadOnlyModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = [JWTAuthentication]
    queryset = Plan.objects.all()

