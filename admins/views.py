from django.shortcuts import render, HttpResponseRedirect
from users.models import Users
from products.models import ProductCategory, Product
from admins.forms import AdminsUserCreationForm, AdminsUserUpdateForm, AdminsCategoryElementForm, AdminsProductElementForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


# 4 контроллера для CRUD
# Главная старница
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'Административная панель GeekShop',
    }
    return render(request, 'admins/index.html', context)


# Список пользователей
@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': Users.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


# Добавление пользователя
@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = AdminsUserCreationForm(data=request.POST, files=request.FILES)  # Важный момент с передачей файла!
        if form.is_valid():
            form.save()
            # сообщение не нужно, поскольку в случае успеха мы перейдем на страницу с перечнем пользователей
            return HttpResponseRedirect(reverse('admins:admin_users'))
        # else:
        # print(form.errors) # это мы вывели ошибки валидации формы в отладке
    else:
        form = AdminsUserCreationForm()

    context = {
        'title': 'GeekShop - Новый пользователь',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


# Изменение пользователя
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = Users.objects.get(id=pk)
    # это тот пользователь на которого кликнули по ссылке на странице пользователей админки
    if request.method == 'POST':
        form = AdminsUserUpdateForm(instance=selected_user,
                                    data=request.POST)  # сказали что менять будем у этого пользователя, которого выбрали на странице
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = AdminsUserUpdateForm(
            instance=selected_user)  # передали текущего пользователя для отображания его «ТТХ» через GET запрос
    context = {
        'title': 'GeekShop - Изменение профиля пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# удаление пользователя
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    selected_user = Users.objects.get(id=pk)
    # selected_user.delete()
    # физическое удаление пользователя из БД. удаление через is_active сделаю позже, но сразу... до того как буду делать защиту через декоратор.
    if selected_user.is_active == True:
        selected_user.is_active = False
    else:
        selected_user.is_active = True
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

#Категории товаров
@user_passes_test(lambda u: u.is_staff)
def admin_categorys(request):
    context = {
        'title': 'GeekShop - категории',
        'categorys': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-category-read.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_categorys_create(request):
    if request.method == 'POST':
        form=AdminsCategoryElementForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categorys'))
    else:
        form = AdminsCategoryElementForm()
    context = {
        'title': 'GeekShop - категории',
        'form': form,
    }
    return render(request, 'admins/admin-category-create.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_categorys_update(request, key):
    print('\n\n',key,'\n\n')
    selected_category = ProductCategory.objects.get(id=key)
    if request.method == 'POST':
        form=AdminsCategoryElementForm(instance = selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categorys'))
    else:
        form = AdminsCategoryElementForm(instance = selected_category)
    context = {
        'title': 'GeekShop - категории',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admin-category-update-delete.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_categorys_delete(request, key):
    selected_category = ProductCategory.objects.get(id=key)
    selected_category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categorys'))

#Товары
@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context = {
        'title': 'GeekShop - товары',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-products-read.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_products_create(request):
    if request.method == 'POST':
        form=AdminsProductElementForm(data=request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = AdminsProductElementForm()
    context = {
        'title': 'GeekShop - новый товар',
        'form': form,
    }
    return render(request, 'admins/admin-products-create.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_products_update(request, key):
    selected_product = Product.objects.get(id=key)
    if request.method == 'POST':
        form=AdminsProductElementForm(instance = selected_product, files = request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = AdminsProductElementForm(instance = selected_product)
    context = {
        'title': 'GeekShop - редактирование товара',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_products_delete(request, key):
    selected_product = Product.objects.get(id=key)
    selected_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))
