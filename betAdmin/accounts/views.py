from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from betAdmin.accounts.forms.registration import RegistrationForm
from betAdmin.accounts.tokens import account_activation_token


def register(request):
    template_name = 'signup.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = RegistrationForm()
            email.send_mail(user, request)
            return redirect(settings.LOGIN_URL)

    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token) and user.profile.email_confirmed is False:
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
