from django.shortcuts import render
from .models import TeslaCar, Dealership # Додаємо Dealership, якщо потрібно буде його відображати пізніше

def car_list(request):
    """
    Представлення для відображення списку всіх автомобілів Tesla.
    """
    cars = TeslaCar.objects.all().order_by('-date_added') # Отримуємо всі автомобілі з бази даних, сортуємо за датою додавання
    context = {
        'cars': cars # Передаємо список автомобілів у шаблон
    }
    return render(request, 'cars/car_list.html', context)