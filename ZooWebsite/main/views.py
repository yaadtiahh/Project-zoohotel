from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Review


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


def about(request):
    return render(request, 'about.html')


def reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews.html', {'reviews': reviews})


def add_review(request):
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        avatar = request.FILES.get("avatar")

        if name and text:
            review = Review.objects.create(name=name, text=text, avatar=avatar)
            avatar_url = review.avatar.url if review.avatar else None
            return JsonResponse({
                "success": True,
                "name": review.name,
                "text": review.text,
                "avatar": avatar_url,
                "created_at": review.created_at.strftime("%d.%m.%Y %H:%M")
            })
        return JsonResponse({"success": False, "error": "Все поля обязательны."})
    return JsonResponse({"success": False, "error": "Только POST-запросы допустимы."})
