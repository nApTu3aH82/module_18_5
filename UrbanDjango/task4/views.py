from django.shortcuts import render


def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/platform.html', context)


def flowers(request):
    title = 'Цветы'
    context = {
        'title': title,
        'flowers': ['Розы', 'Тюльпаны', 'Герберы', 'Гвоздики']
    }
    return render(request, 'fourth_task/flowers.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/cart.html', context)
# Create your views here.
