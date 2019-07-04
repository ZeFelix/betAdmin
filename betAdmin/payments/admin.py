from django.contrib import admin
from betAdmin.payments.models import Payment, AdministratorAccount

admin.site.register(Payment)
admin.site.register(AdministratorAccount)

