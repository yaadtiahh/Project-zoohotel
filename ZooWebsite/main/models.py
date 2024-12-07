from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")  # Поле для аватара
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name}: {self.text[:20]}"
