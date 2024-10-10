from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'fourth_task/home.html', {'pagename': 'Главная страница'})

def shop(request):
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин'})

def cart(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина', 'games': ['Atomic Heart',
                                                                                      'Cyberpunk 2077']})