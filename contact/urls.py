from django.urls import path

from . import views

app_name = 'contact'


urlpatterns = [
    path('<int:contact_id>/', views.contact_view, name='contact_view'),
    path('', views.index_view, name='index'),
]
