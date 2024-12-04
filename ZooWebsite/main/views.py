from django.shortcuts import render  # , get_object_or_404
# from .models import News


# Функциональное представление для домашней страницы
def index(request):
    return render(request, 'index.html')  # Убедитесь, что шаблон 'index.html' существует
