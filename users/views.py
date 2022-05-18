from django.shortcuts import render

def index(request):

    return render(request, 'users/new.html')


def detail(request, user_id):

    return render(request, 'users/detail.html')