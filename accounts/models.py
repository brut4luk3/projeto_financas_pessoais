from django.db import models

from users.models import User

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_account')
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_account')
    value = models.FloatField(default=0)
    timestamp = models.DateTimeField()