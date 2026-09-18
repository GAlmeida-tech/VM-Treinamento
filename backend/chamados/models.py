from django.db import models

# Create your models here.
class Chamados(models.Model):

    PRIORIDADE_LIST = [
        ('alta', 'Alta'),
        ('média','Média'),
        ('baixa','Baixa'),
    ]

    STATUS_LIST = [
            ('aberto','Aberto'),
            ('em andamento','Em andamento'),
            ('fechado','Fechado'),
        ]


    titulo = models.CharField(max_length= 40)
    solicitante = models.CharField(max_length= 40)
    descricao = models.TextField
    prioridade = models.CharField(choices= PRIORIDADE_LIST, max_length= 13)
    status = models.CharField(choices= STATUS_LIST, max_length= 12)