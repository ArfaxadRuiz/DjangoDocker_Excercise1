from django.urls import path
from .views import prueba_lista

urlpatterns = [
    path('productos/', prueba_lista.as_view(), name='product-list'),
]
