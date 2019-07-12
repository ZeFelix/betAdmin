from django.contrib import admin
from betAdmin.payments.models import Payment, AdministratorAccount, Plan

admin.site.register(Payment)
admin.site.register(AdministratorAccount)
admin.site.register(Plan)

