from django.views.generic import ListView
from .models import ProductModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import ProductModel
from .models import Producto


class prueba_lista(ListView):
    model = ProductModel
    template_name = 'e_commerce/product_list.html'
    context_object_name = 'productos'

class ProtectedListView(LoginRequiredMixin, ListView):
    model = ProductModel
    template_name = "products/protected_list.html"
    context_object_name = "products"
    login_url = "/login/"
    redirect_field_name = "next"

    def get_queryset(self):
        # Solo productos del usuario logueado
        return Producto.objects.filter(user=self.request.user)