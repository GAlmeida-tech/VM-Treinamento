from django.urls import include, path
from . import views

urlpatterns = [
    path('chamados/', views.chamados_list, name='chamados-list'),

]