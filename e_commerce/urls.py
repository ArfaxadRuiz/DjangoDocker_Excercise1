from django.urls import path
from django.contrib.auth import views as auth_views
from .views import prueba_lista, ProtectedListView

urlpatterns = [
    path('productos/', prueba_lista.as_view(), name='product-list'),

    # vista protegida
    path("productos-protegidos/", ProtectedListView.as_view(), name="protected_products"),

    # login/logout de Django
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
