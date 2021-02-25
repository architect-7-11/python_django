from django.shortcuts import render,redirect

# Create your views here.
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout #kullanıcı sorgusu için
from django.contrib import messages


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    
        newUser = User(username= username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"başarıyla kayıt oldunuz")
        return redirect("index")


    form = RegisterForm()
    context = {
        "form":form
    }
    return render(request,"register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"kullanıcı adı veya şifre hatalı ")
            return render(request,"login.html",context)

        messages.success(request,"başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")


    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"başarıyla çıkış yaptınız")
    return redirect("index")







