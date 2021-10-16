from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

def login (request):
    # это обрабатывается POST
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid(): # если данные в форме валидны (а данные тут - кусок html кода)
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) # результат прохождения аутентификации
            if user and user.is_active:
                auth.login(request, user) # авторизоваться этим пользователем
                return HttpResponseRedirect(reverse('index')) # перенаправить на главную
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    # Это обрабатывается GET запрос
    context = {
        'title': 'Авторизация в GeekShop',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context= {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request,'users/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))