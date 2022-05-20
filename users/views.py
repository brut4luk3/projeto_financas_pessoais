from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from accounts.models import Account
from .models import User

def index(request):

    total_num_accounts = request.user.account_set.all().count()

    context = {
        'total_num_accounts': total_num_accounts
    }

    return render(request, 'users/index.html', context=context)


def detail(request: HttpRequest, user_id: int):

    return render(request, 'users/detail.html')


def create_account(request):

    if request.method == 'GET':
        return render(request, 'accounts/create.html')

    elif request.method == 'POST':

        post_data = request.POST

        if len(post_data.get("txtInitialBalance").strip()):
            balance = float(post_data.get("txtInitialBalance").strip())

        else:
            balance = 0

        account = Account(
            user_id=request.user,
            name=post_data.get('txtAccountName'),
            balance=balance
        )

        account.save()

        return HttpResponseRedirect(reverse('users:list_accounts',))


def list_accounts(request):

    user_accounts = request.user.account_set.all()

    context = {
        'user_accounts': user_accounts
    }

    return render(request, 'accounts/list.html', context=context)