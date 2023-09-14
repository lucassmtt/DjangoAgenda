from django.urls import path

from . import views

app_name = 'contact'


urlpatterns = [
    path('<int:contact_id>/', views.contact_view, name='contact_view'),
    path('search/', views.search, name='search'),  # type: ignore
    path('', views.index_view, name='index'),
]
