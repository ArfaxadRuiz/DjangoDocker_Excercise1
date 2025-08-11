from django.views.generic import ListView
from .models import ProductModel

class prueba_lista(ListView):
    model = ProductModel
    template_name = 'e_commerce/product_list.html'
    context_object_name = 'productos'