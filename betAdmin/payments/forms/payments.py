from django import forms

from betAdmin.payments.models import Payment, AdministratorAccount, Plan

class SavePaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['payment_method', 'adm_account', 'plan','file']
        file = forms.FileField(required = False)
        widgets = {
            'payment_method' : forms.Select(choices=Payment.PAYMENT_CHOICES, attrs = {'placeholder': 'Método de pagamento'}),
            'plan' : forms.Select(choices=Payment.PAYMENT_CHOICES, attrs = {'placeholder': 'Selecione o tipo de plano'}),
            'adm_account' : forms.Select(choices=AdministratorAccount.CHECKING_ACCOUNT, attrs = {'placeholder': 'Selecione a conta', 'onchange':"changeAccountPayment(this)"}),
        }