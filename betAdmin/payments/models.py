import datetime
from django.db import models
from django.contrib.auth.models import User


class AdministratorAccount(models.Model):
    CHECKING_ACCOUNT = 'CC'
    SAVINGS_ACCOUNT = 'CP'
    ACCOUNT_CHOICES = [
        (CHECKING_ACCOUNT, 'checking account'),
        (SAVINGS_ACCOUNT, 'savings account'),
    ]

    name = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50, null=True)
    bank_number = models.CharField(max_length=10, null=True)
    agency = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10)
    digit = models.CharField(max_length=2)
    op = models.CharField(max_length=5)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_CHOICES, default=SAVINGS_ACCOUNT)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'payments_administrator_account'


class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    day = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = 'payments_plan'


class Payment(models.Model):
    CREDIT_CARD = 'CC'
    TICKET = 'TK'
    TRANSFER = 'TR'
    DEPOSIT = 'DP'
    PAYMENT_CHOICES = [
        (CREDIT_CARD, 'credit card'),
        (TICKET, 'ticket'),
        (TRANSFER, 'transfer'),
        (DEPOSIT, 'deposit'),
    ]

    def payment_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/payments/user_<id>/<filename>
        return 'payments/{0}/{1}'.format(instance.user.id, filename)

    value = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default=TRANSFER)
    is_paid = models.BooleanField(default=False)
    file = models.FileField(upload_to=payment_directory_path, max_length=100)
    user = models.ForeignKey(User, related_name='payments_user', on_delete=models.CASCADE)
    adm_account = models.ForeignKey(AdministratorAccount, related_name='payments_adm_account', on_delete=models.CASCADE)

    def active_payment(self, user):
        payment = Payment.objects.filter(user=user).filter(is_paid=True).order_by('expiration_date').reverse().first()
        try:
            if payment.expiration_date >= datetime.datetime.today().date():
                return payment
            else:
                return None
        except:
            return None

    def pendent_payment(self, user):
        payment = Payment.objects.filter(user=user).filter(is_paid=False).first()
        if payment:
            return payment
        else:
            return False
