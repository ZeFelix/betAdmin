from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from betAdmin.accounts.tokens import account_activation_token
from core.mail import send_mail_template


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já existe está cadastrado.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def send_mail(self, user, request):
        subject = 'Link de Ativação de Conta'
        current_site = get_current_site(request)

        message = {
            'user': user, 'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }

        template_name = 'acc_active_email.html'

        send_mail_template(
            subject, template_name, message, ['caetanov120@gmail.com']
        )
