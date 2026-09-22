from django.urls import path
from . import views

urlpatterns = [
    path('chamados/', views.chamados_view, name='chamados-list'),
    path('chamados/<int:id>/', views.delete_view, name='chamados-delete'),
    
]