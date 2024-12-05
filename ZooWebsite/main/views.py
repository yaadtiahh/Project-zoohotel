from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


# Функциональное представление для домашней страницы
def index(request):
    if request.method == "POST":
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dates = request.POST.get('dates')

        # Формируем сообщение
        message = f"Новая заявка на бронирование:\n\nИмя: {name}\nТелефон: {phone}\nДаты: {dates}"

        # Отправляем email
        send_mail(
            subject="Новая заявка на бронирование",
            message=message,
            from_email="yar.sol08162006@gmail.com",    # Ваш email
            recipient_list=["egor.kuken@gmail.com"],  # Email получателя
            fail_silently=False,
        )

        return HttpResponse("Спасибо! Ваша заявка отправлена.")

    return render(request, "index.html")


def services(request):
    return render(request, 'services.html')


def prices(request):
    return render(request, 'prices.html')
