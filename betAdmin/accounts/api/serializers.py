from rest_framework.serializers import ModelSerializer

from betAdmin.accounts.models import Profile


class SimpleProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'first_name', 'email_confirmed']