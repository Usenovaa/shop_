from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название', unique=True)
    slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
