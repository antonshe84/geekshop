"""
это модуль обеспечивающий работу пространства адресов приложения «админка»
"""
from django.urls import path
from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete, admin_categorys, admin_categorys_create, admin_categorys_delete, admin_categorys_update, admin_products, admin_products_create, admin_products_update, admin_products_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name = 'index'),
# управление пользователями
    path('users/', admin_users, name = 'admin_users'),
    path('users-create/', admin_users_create, name = 'admin_users_create'),
    path('users-update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>/', admin_users_delete, name='admin_users_delete'),
# управление категориями
    path('categorys/', admin_categorys, name = 'admin_categorys'),
    path('categorys-create/', admin_categorys_create, name = 'admin_categorys_create'),
    path('categorys-update/<int:key>/', admin_categorys_update, name = 'admin_categorys_update'),
    path('categirys-delete/<int:key>/', admin_categorys_delete, name = 'admin_categorys_delete'),
# управление товарами
    path('products/', admin_products, name = 'admin_products'),
    path('products-create/', admin_products_create, name = 'admin_products_create'),
    path('products-update/<int:key>/', admin_products_update, name = 'admin_products_update'),
    path('products-delete/<int:key>/', admin_products_delete, name = 'admin_products_delete'),
]