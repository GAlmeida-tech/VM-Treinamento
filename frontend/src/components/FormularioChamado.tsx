import { useState, type FormEvent } from 'react'
import type { Chamado, DadosChamado } from '../api/chamados'

const VAZIO: DadosChamado = {
  titulo: '',
  descricao: '',
  solicitante: '',
  prioridade: 'média',
  status: 'aberto',
}

interface Props {
  // Quando vem um chamado, o formulário está em modo edição
  chamadoEmEdicao: Chamado | null
  salvando: boolean
  onSalvar: (dados: DadosChamado) => void
  onCancelar: () => void
}

export function FormularioChamado({ chamadoEmEdicao, salvando, onSalvar, onCancelar }: Props) {
  const [dados, setDados] = useState<DadosChamado>(chamadoEmEdicao ?? VAZIO)

  function alterar<K extends keyof DadosChamado>(campo: K, valor: DadosChamado[K]) {
    setDados((atual) => ({ ...atual, [campo]: valor }))
  }

  function enviar(evento: FormEvent) {
    evento.preventDefault()
    onSalvar(dados)
    if (!chamadoEmEdicao) {
      setDados(VAZIO)
    }
  }

  return (
    <form className="formulario" onSubmit={enviar}>
      <h2>{chamadoEmEdicao ? `Editar chamado #${chamadoEmEdicao.id}` : 'Novo chamado'}</h2>

      <label>
        Título
        <input
          value={dados.titulo}
          onChange={(e) => alterar('titulo', e.target.value)}
          maxLength={120}
          required
        />
      </label>

      <label>
        Solicitante
        <input
          value={dados.solicitante}
          onChange={(e) => alterar('solicitante', e.target.value)}
          maxLength={100}
          required
        />
      </label>

      <label>
        Descrição
        <textarea
          value={dados.descricao}
          onChange={(e) => alterar('descricao', e.target.value)}
          rows={4}
          required
        />
      </label>

      <div className="linha">
        <label>
          Prioridade
          <select
            value={dados.prioridade}
            onChange={(e) => alterar('prioridade', e.target.value as DadosChamado['prioridade'])}
          >
            <option value="baixa">Baixa</option>
            <option value="média">Média</option>
            <option value="alta">Alta</option>
          </select>
        </label>

        <label>
          Status
          <select
            value={dados.status}
            onChange={(e) => alterar('status', e.target.value as DadosChamado['status'])}
          >
            <option value="aberto">Aberto</option>
            <option value="em andamento">Em andamento</option>
            <option value="fechado">Fechado</option>
          </select>
        </label>
      </div>

      <div className="acoes">
        <button type="submit" disabled={salvando}>
          {salvando ? 'Salvando...' : chamadoEmEdicao ? 'Salvar alterações' : 'Abrir chamado'}
        </button>
        {chamadoEmEdicao && (
          <button type="button" className="secundario" onClick={onCancelar}>
            Cancelar
          </button>
        )}
      </div>
    </form>
  )
}
