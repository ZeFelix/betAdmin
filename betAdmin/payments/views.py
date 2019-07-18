import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from betAdmin.payments.models import AdministratorAccount, Plan, Payment
from betAdmin.payments.forms.payments import SavePaymentForm
from dateutil.relativedelta import *


class PaymentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        template_name = 'sign_plan.html'

        payment = Payment()

        payment_pendent = payment.pendent_payment(request.user)

        payment_instance = payment_pendent if payment_pendent else None

        context = {
            'payment_pendent': payment_pendent,
            'payment_active': payment.active_payment(request.user),
            'form' : SavePaymentForm(instance=payment_instance)
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        template_name = 'sign_plan.html'

        context = {}
        payment_form = SavePaymentForm(request.POST)
        payment_form.instance.user_id = request.user.pk
        payment_form.instance.payment_date = datetime.datetime.today().date()

        if payment_form.is_valid():
            active = payment_form.instance.active_payment(request.user)
            if active:
                payment_form.instance.expiration_date = active.expiration_date + relativedelta(months=payment_form.instance.plan.day)
            else:
                payment_form.instance.expiration_date = datetime.datetime.today() + relativedelta(months=payment_form.instance.plan.day)
        
            payment_form.save()
         
            return HttpResponseRedirect(reverse('payments:sign_plan'))

        return render(request, template_name, context)


class PaymentViewUpdated(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        template_name = "sign_plan.html"
        payment = Payment.objects.get(pk=pk)
        if request.FILES.get('file'):
            payment.file = request.FILES['file']
        payment.save()
        return HttpResponseRedirect(reverse('payments:sign_plan'))


class PaymentViewDelete(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        return HttpResponseRedirect(reverse('payments:sign_plan'))