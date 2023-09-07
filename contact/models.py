from django.db import models
from django .utils import timezone

# First:
# id (primary key - automatic)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# After:
# category (foreign key), show (boolean), owner (foreign key)
# picture (image)


class Contact(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

