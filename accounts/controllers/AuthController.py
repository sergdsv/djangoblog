from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ..forms import UsersLoginForm
from django.shortcuts import redirect


def login_user(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "form.html", {
        "form": form,
        "title": "Login",
    })


def logout_view(request):
    logout(request)
    return redirect('login')
