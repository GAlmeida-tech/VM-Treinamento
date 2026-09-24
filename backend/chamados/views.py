from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Chamados
from .serializers import Chamados_Serializers
from django.conf import settings



def verificacao(view_original):
    def funcao_nova(request, *args, **kwargs):
        chave_autorizacao = request.headers.get('API-KEY')
        if chave_autorizacao == settings.API_KEY:
            return view_original(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return funcao_nova




@api_view(['GET', 'POST'])
@verificacao
def chamados_view(request):
    if request.method == 'GET':
        chamados = Chamados.objects.all()
        serializado = Chamados_Serializers(instance=chamados, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializado = Chamados_Serializers(data= request.data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
@verificacao
def chamado_detalhe(request, id):
    try:
        chamado = Chamados.objects.get(id=id)
    except Chamados.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        chamado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializado = Chamados_Serializers(instance=chamado, data=request.data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=status.HTTP_200_OK)
        else:
            return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

