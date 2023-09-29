from django.urls import path
from produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('detalhe/<slug>/', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionaraocarrinho/', views.AdicionarCarrinho.as_view(), name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverCarrinho.as_view(), name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name='resumodacompra'),

]
