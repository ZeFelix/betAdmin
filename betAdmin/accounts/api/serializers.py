from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from betAdmin.accounts.models import Profile


class SimpleProfileSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Profile.objects.all())])

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'first_name', 'email_confirmed', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
