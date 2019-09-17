from rest_framework.serializers import ModelSerializer

from betAdmin.payments.models import AdministratorAccount


class AdministratorAccountSerializer(ModelSerializer):
    class Meta:
        model = AdministratorAccount
        fields = [
            'name', 'bank_name', 'bank_number',
            'agency', 'account_number', 'digit', 'op', 'account_type'
        ]
