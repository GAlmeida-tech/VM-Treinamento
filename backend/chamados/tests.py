from rest_framework import status
from rest_framework.test import APITestCase

dados = {
    'titulo': 'Impressora do RH',
    'descricao': 'Luz laranja piscando',
    'solicitante': 'Maria',
    'prioridade': 'alta',
    'status': 'aberto',
    }


class ChamadoApiTests(APITestCase):

#TESTE DE POST
    def  test_cria_chamado(self):

        resposta_Post = self.client.post('/api/chamados/', dados, format='json')

        self.assertEqual(resposta_Post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resposta_Post.data['descricao'], 'Luz laranja piscando')


# TESTE DE GET
    def test_lista_chamados(self):

        resposta_Get = self.client.get('/api/chamados/', dados, format='json')
        self.assertEqual(resposta_Get.status_code, status.HTTP_200_OK)


#TESTE DE PUT
    def test_edita_chamado(self):
        chamadoCriado = self.client.post('/api/chamados/', dados, format='json')
        id_chamado = chamadoCriado.data['id']

        dados['titulo'] = "luizinha da impressora piscando laranja no setor do RH"

        resposta_Put = self.client.put(f'/api/chamados/{id_chamado}/', dados, format='json')
        self.assertEqual(resposta_Put.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta_Put.data['titulo'], 'luizinha da impressora piscando laranja no setor do RH')


       
 # TESTE DELETE
    def test_exclui_chamado(self):
        chamadoCriado = self.client.post('/api/chamados/', dados, format='json')
        id_chamado = chamadoCriado.data['id']
         
        resposta_Delete = self.client.delete(f'/api/chamados/{id_chamado}/')
        self.assertEqual(resposta_Delete.status_code, status.HTTP_204_NO_CONTENT) 



 #TESTE 404
    def test_chamado_inexistente_retorna_404(self):
        chamadoCriado = self.client.post('/api/chamados/', dados, format='json')
        id_chamado = chamadoCriado.data['id']
         
        resposta_Delete = self.client.delete(f'/api/chamados/{id_chamado}/')

        resposta_404 = self.client.get(f'/api/chamados/{resposta_Delete}/', format='json')
        self.assertEqual(resposta_404.status_code, status.HTTP_404_NOT_FOUND)

            
