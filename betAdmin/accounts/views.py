from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from betAdmin.accounts.forms.registration import RegistrationForm, EditAccountForm
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


@login_required()
def profile(request):
    template_name = 'profile.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            context['success'] = {
                'header' : 'Atualização',
                'content' : '{0} atualizado com sucesso!'.format(request.user)
            }
    else:
        form = EditAccountForm(instance=request.user.profile)

    context['form'] = form

    return render(request, template_name, context)


@login_required()
def resend_email(request):
    email = RegistrationForm()
    email.send_mail(request.user, request)
    return redirect(request.META.get('HTTP_REFERER'))


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token) and not user.profile.email_confirmed:
        user.profile.email_confirmed = True
        user.profile.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
