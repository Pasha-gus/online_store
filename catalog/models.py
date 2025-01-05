from django.db import models

from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование")
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="media/image", verbose_name="Фотографии", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="category",
    )
    purchase_price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(null=True, verbose_name="Дата создания")
    updated_at = models.DateField(null=True, verbose_name="Обновленно")
    publication_status = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец продукта",
        null=True,
        blank=True,
        related_name="user"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category"]
        permissions = [
            ('can_unpublish_product', 'can unpublish product')
        ]
