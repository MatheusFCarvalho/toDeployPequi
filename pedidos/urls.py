from django.urls import path
from . import views

app_name = 'pedidos'  # Opcional: Defina o namespace do aplicativo

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('produtor/', views.produtor, name='produtor'),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('reset/', views.resetPedidos, name='reset_pedidos'),
    # Adicione outras URLs do aplicativo aqui
]
