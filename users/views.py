from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from baskets.models import Basket
from django.contrib.auth.decorators import login_required


def login(request):
    # это обрабатывается POST
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():  # если данные в форме валидны (а данные тут - кусок html кода)
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # результат прохождения аутентификации
            if user and user.is_active:
                auth.login(request, user)  # авторизоваться этим пользователем
                return HttpResponseRedirect(reverse('index'))  # перенаправить на главную
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
            messages.success(request, 'Вы успешно зарегистрировались! Введите ваш аватар в личном кабинете')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения успешно сохранены!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Профиль пользователя',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)
