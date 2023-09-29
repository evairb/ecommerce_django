from django.urls import path
from pedido import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name='pagar'),
    path('salvarpedido/', views.SalvarPedido.as_view(), name='salvarpedido'),
    path('detalhe/', views.DetalhesPedido.as_view(), name='detalhe'),
]
