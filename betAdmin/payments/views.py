import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from betAdmin.payments.models import AdministratorAccount, Plan, Payment
from dateutil.relativedelta import *


@login_required()
def sign_plan(request):
    template_name = 'sign_plan.html'

    if request.method == 'POST':
        form = request.POST
        plan = Plan.objects.get(id=form['select_plan'])
        account = AdministratorAccount.objects.get(id=form['select_account'])

        payment = Payment()
        payment.user = request.user
        payment.value = plan.price
        payment.adm_account_id = account.id
        payment.payment_method = 'DP'
        payment.payment_date = datetime.datetime.today().date()

        active = payment.active_payment(request.user)
        if active:
            payment.expiration_date = active.expiration_date + relativedelta(months=plan.day)
        else:
            payment.expiration_date = datetime.datetime.today() + relativedelta(months=plan.day)

        payment.save()

        return HttpResponseRedirect(reverse('payments:sign_plan'))

    accounts = AdministratorAccount.objects.all()
    plans = Plan.objects.all()
    payment = Payment()

    context = {
        'accounts': accounts,
        'plans': plans,
        'payment_pendent': payment.pendent_payment(request.user),
        'payment_active': payment.active_payment(request.user)
    }

    return render(request, template_name, context)
