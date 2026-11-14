from django.db import models


class Review(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    email = models.EmailField("Email")
    text = models.TextField("Текст отзыва")
    approved = models.BooleanField("Проверено", default=False)
