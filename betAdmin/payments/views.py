import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from betAdmin.payments.models import AdministratorAccount, Plan, Payment
from dateutil.relativedelta import *


class PaymentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        template_name = 'sign_plan.html'
        
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

    def post(self, request, *args, **kwargs):
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