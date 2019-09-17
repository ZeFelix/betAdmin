from rest_framework.serializers import ModelSerializer

from betAdmin.payments.models import AdministratorAccount, Plan


class AdministratorAccountSerializer(ModelSerializer):
    class Meta:
        model = AdministratorAccount
        fields = [
            'ACCOUNT_CHOICES', 'name', 'bank_name', 'bank_number',
            'agency', 'account_number', 'digit', 'op', 'account_type'
        ]


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'day', 'price']