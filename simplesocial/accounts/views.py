from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'

    # 'login' url is loaded only AFTER the user has Signed Up
    # 'reverse' is used to access the LINK corresponding to the url name 'login'
    success_url = reverse_lazy('login')