from django.shortcuts import render
import datetime
import json


def index(request):
    context = {
        'title': 'Интернет-магазин GeekShop (учебный проект на Django)'
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('products/templates/db.json', 'r') as f:
        products_data = json.load(f)

    print(products_data)

    context = {
        'title': 'GeekShop - каталог наших предложений',
        'date': datetime.datetime.now().today(),
        'products': products_data
        # 'products': [
        #     {'name': 'Худи черного цвета с монограммами adidas Originals',
        #      'img': '/vendor/img/products/Adidas-hoodie.png',
        #      'price': 6900,
        #      'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'
        #      },
        #
        #     {'name': 'Синяя куртка The North Face',
        #      'img': '/vendor/img/products/Blue-jacket-The-North-Face.png',
        #      'price': 23725,
        #      'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель'
        #      },
        #
        #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #      'img': '/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        #      'price': 3390,
        #      'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
        #      },
        #
        #     {'name': 'Черный рюкзак Nike Heritage',
        #      'img': '/vendor/img/products/Black-Nike-Heritage-backpack.png',
        #      'price': 2340,
        #      'description': 'Плотная ткань. Легкий материал.'
        #      },
        #
        #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        #      'img': '/vendor/img/products/Black-Dr-Martens-shoes.png',
        #      'price': 13590,
        #      'description': 'Гладкий кожаный верх. Натуральный материал.'
        #      },
        #
        #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        #      'img': '/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
        #      'price': 2890,
        #      'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
        #      },
        # ]
    }
    return render(request, 'products/products.html', context)
