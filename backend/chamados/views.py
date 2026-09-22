from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Chamados
from .serializers import Chamados_Serializers

@api_view(['GET', 'POST'])
def chamados_view(request):
    if request.method == 'GET':
        chamados = Chamados.objects.all()
        serializado = Chamados_Serializers(instance=chamados, many=True)
        return Response(serializado.data)

    elif request.method == 'POST':
        serializado = Chamados_Serializers(data= request.data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data)
            
        else:
            return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)
