from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from betAdmin.accounts.api.serializers import SimpleProfileSerializer
from betAdmin.accounts.models import Profile


class SimpleProfileViewSet(ModelViewSet):
    serializer_class = SimpleProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [JWTAuthentication]
