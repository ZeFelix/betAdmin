from django.urls import path
from betAdmin.payments.views import PaymentView, PaymentViewUpdated

app_name = 'payments'

urlpatterns = [
    path('sign_plan/', PaymentView.as_view(), name='sign_plan'),
    path('sign_plan/<int:pk>', PaymentViewUpdated.as_view(), name='sign_plan_updated'),
]