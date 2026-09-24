from rest_framework import status
from rest_framework.test import APITestCase
from django.conf import settings




    



class ChamadoApiTests(APITestCase):
    def setUp(self):
        self.headers = {'HTTP_API_KEY': settings.API_KEY}


    def test_cria_chamado_com_descricao(self):
        dados = {
            'titulo': 'Impressora do RH',
            'descricao': 'Luz laranja piscando',
            'solicitante': 'Maria',
            'prioridade': 'alta',
            'status': 'aberto',
        }


#TESTE DE POST
        respostaPost = self.client.post('/api/chamados/', dados, format='json', **self.headers)

        self.assertEqual(respostaPost.status_code, status.HTTP_201_CREATED)
        self.assertEqual(respostaPost.data['descricao'], 'Luz laranja piscando')


# TESTE DE GET
        respostaGet = self.client.get('/api/chamados/', dados, format='json', **self.headers)

        

        self.assertEqual(respostaGet.status_code, status.HTTP_200_OK)
        self.assertEqual(respostaGet.data[0]['titulo'], 'Impressora do RH')
        self.assertEqual(respostaGet.data[0]['descricao'], 'Luz laranja piscando')


# TESTE DELETE
        chamado_id = respostaPost.data['id']

        respostaDelete = self.client.delete(f'/api/chamados/{chamado_id}/', **self.headers)
        self.assertEqual(respostaDelete.status_code, status.HTTP_204_NO_CONTENT)

