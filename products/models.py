from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(verbose_name='название продукта', max_length=256)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение продукта', blank=True, upload_to='product_img')
    price = models.DecimalField(verbose_name='стоимость', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.category.name})"


"""
    Для загрузки данных в базу выполнить в корне проекта:
    python manage.py loaddata products/fixtures/category.json
    python manage.py loaddata products/fixtures/products.json
    
    До этого удалить миграции и базу данных и выполнить повторно:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
"""