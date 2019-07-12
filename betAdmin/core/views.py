import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from betAdmin.payments.models import Payment


@login_required()
def index(request):
    template_name = 'index.html'

    payment = Payment()

    context = {
        'payment': payment.active_payment(request.user)
    }
    return render(request, template_name, context)
