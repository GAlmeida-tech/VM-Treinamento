from django.db import models

# Create your models here.
class Chamados(models.Model):

    PRIORIDADE_LIST = [
        ('alta', 'Alta'),
        ('media','Média'),
        ('baixa','Baixa'),
    ]

    STATUS_LIST = [
        ('aberto','Aberto'),
        ('em_andamento','Em andamento'),
        ('fechado','Fechado'),
    ]


    titulo = models.CharField(max_length= 120)
    solicitante = models.CharField(max_length= 100)
    descricao = models.TextField()
    prioridade = models.CharField(choices= PRIORIDADE_LIST, max_length= 13)
    status = models.CharField(choices= STATUS_LIST, max_length= 20)
    criado_em = models.DateTimeField(auto_now_add=True)