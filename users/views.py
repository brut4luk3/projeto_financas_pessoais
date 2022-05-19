from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from accounts.models import Account
from .models import User

def index(request):

    total_num_accounts = request.user.account_set.all().count()

    context = {
        'total_num_accounts': total_num_accounts
    }

    return render(request, 'users/index.html', context=context)


def detail(request, user_id):

    return render(request, 'users/detail.html')