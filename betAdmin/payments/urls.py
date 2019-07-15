from django.urls import path
from betAdmin.payments.views import PaymentView

app_name = 'payments'

urlpatterns = [
    path('sign_plan/', PaymentView.as_view(), name='sign_plan'),
]