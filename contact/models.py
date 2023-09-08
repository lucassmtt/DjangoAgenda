from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# First:
# id (primary key - automatic)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# After:
# category (foreign key), show (boolean), owner (foreign key)
# picture (image)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f'Name of category: {self.name}, Description: {self.description}'


class Contact(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Name: {self.first_name}, Lastname: {self.last_name}'
