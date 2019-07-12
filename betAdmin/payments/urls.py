from django.urls import path
from betAdmin.payments import views

app_name = 'payments'

urlpatterns = [
    path('sign_plan/', views.sign_plan, name='sign_plan')
]