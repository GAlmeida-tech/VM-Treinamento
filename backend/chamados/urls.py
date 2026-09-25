from django.urls import path
from . import views

urlpatterns = [
    path('chamados/', views.chamados_view, name='chamados_lista'),
    path('chamados/<int:id>/', views.chamado_detalhe, name='chamado_detalhe'),
    
]