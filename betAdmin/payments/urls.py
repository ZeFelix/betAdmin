from django.urls import path
from betAdmin.payments.views import PaymentView, PaymentViewUpdated, PaymentViewDelete

app_name = 'payments'

urlpatterns = [
    path('sign_plan/', PaymentView.as_view(), name='sign_plan'),
    path('sign_plan/<int:pk>/update', PaymentViewUpdated.as_view(), name='sign_plan_updated'),
    path('sign_plan/<int:pk>/delete', PaymentViewDelete.as_view(), name='sign_plan_delete'),
]