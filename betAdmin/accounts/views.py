from django.conf import settings
from django.shortcuts import render, redirect

from betAdmin.accounts.forms.registration import RegistrationForm


def register(request):
    template_name = 'signup.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)

    else:
        form = RegistrationForm()

    context = {
        'form':form
      }
    
    return render(request, template_name, context)
