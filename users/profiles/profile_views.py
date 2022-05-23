from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import Profile
from register import views

def show_profile(request):

    return render(request, 'profiles/index.html')