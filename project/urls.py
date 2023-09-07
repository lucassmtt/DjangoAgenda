from django.contrib import admin
from django.urls import include, path

import contact

urlpatterns = [
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]
