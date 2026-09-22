// Client HTTP dos chamados.
//
// As rotas abaixo AINDA NÃO EXISTEM no Django — criar no backend é o exercício.
// Contrato que o front espera (padrão de um ModelViewSet do DRF):
//
//   GET    /api/chamados/       -> lista de chamados
//   POST   /api/chamados/       -> cria um chamado, devolve o chamado criado
//   PUT    /api/chamados/<id>/  -> atualiza um chamado, devolve o chamado atualizado
//   DELETE /api/chamados/<id>/  -> remove um chamado (204, sem corpo)

export type StatusChamado = 'aberto' | 'em andamento' | 'fechado'

export type Prioridade = 'baixa' | 'média' | 'alta'

export interface Chamado {
  id: number
  titulo: string
  descricao: string
  solicitante: string
  prioridade: Prioridade
  status: StatusChamado
  criado_em: string
}

// O que o formulário envia: o id e a data quem gera é o backend.
export type DadosChamado = Omit<Chamado, 'id' | 'criado_em'>

const URL_BASE = '/api/chamados/'

async function requisitar<T>(url: string, opcoes?: RequestInit): Promise<T> {
  const resposta = await fetch(url, {
    ...opcoes,
    headers: { 'Content-Type': 'application/json', ...opcoes?.headers },
  })

  if (!resposta.ok) {
    throw new Error(`Erro ${resposta.status} em ${opcoes?.method ?? 'GET'} ${url}`)
  }

  // DELETE devolve 204 sem corpo
  if (resposta.status === 204) {
    return undefined as T
  }
  return resposta.json() as Promise<T>
}

export function listarChamados() {
  return requisitar<Chamado[]>(URL_BASE)
}

export function criarChamado(dados: DadosChamado) {
  return requisitar<Chamado>(URL_BASE, {
    method: 'POST',
    body: JSON.stringify(dados),
  })
}

export function atualizarChamado(id: number, dados: DadosChamado) {
  return requisitar<Chamado>(`${URL_BASE}${id}/`, {
    method: 'PUT',
    body: JSON.stringify(dados),
  })
}

export function excluirChamado(id: number) {
  return requisitar<void>(`${URL_BASE}${id}/`, { method: 'DELETE' })
}
