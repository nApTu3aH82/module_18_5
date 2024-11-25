from django.shortcuts import render


def platform(request):
    return render(request, 'third_task/platform.html')


def flowers(request):
    return render(request, 'third_task/flowers.html')


def cart(request):
    return render(request, 'third_task/cart.html')
# Create your views here.
