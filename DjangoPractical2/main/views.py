from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'title': 'Головна сторінка'})

def view1(request):
    return render(request, 'view.html', {'title': 'Вьюшка 1'})

def view2(request):
    return render(request, 'view.html', {'title': 'Вьюшка 2'})

def view3(request):
    return render(request, 'view.html', {'title': 'Вьюшка 3'})

def view4(request):
    return render(request, 'view.html', {'title': 'Вьюшка 4'})


