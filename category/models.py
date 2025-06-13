from django.db import models

TYPE_CHOICE = [
    ('services', 'خدمات'),
    ('products', 'محصولات'),
]


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, default='services', verbose_name='نوع دسته بندی')

    def __str__(self):
        return self.name
