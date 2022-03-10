from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from accounts.forms import LoginForm


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password']
                                )
            if user is None:
                return HttpResponse('Неверный логин или пароль')

            if not user.is_active():
                return HttpResponse('Пользователь неактивен!')

            login(request, user)
            return HttpResponse('Добро пожаловать! Успешный вход')

        return render(request, "accounts/login.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/login.html", {'form': form})
