from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_accounts'

class Transaction(models.Model):
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_account')
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_account')
    value = models.FloatField(default=0)
    timestamp = models.DateTimeField()