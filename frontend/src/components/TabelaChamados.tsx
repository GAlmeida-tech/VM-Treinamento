import type { Chamado, Prioridade, StatusChamado } from '../api/chamados'

const ROTULO_STATUS: Record<StatusChamado, string> = {
  aberto: 'Aberto',
  em_andamento: 'Em andamento',
  fechado: 'Fechado',
}

const ROTULO_PRIORIDADE: Record<Prioridade, string> = {
  baixa: 'Baixa',
  media: 'Média',
  alta: 'Alta',
}

interface Props {
  chamados: Chamado[]
  onEditar: (chamado: Chamado) => void
  onExcluir: (chamado: Chamado) => void
}

export function TabelaChamados({ chamados, onEditar, onExcluir }: Props) {
  if (chamados.length === 0) {
    return <p className="vazio">Nenhum chamado cadastrado.</p>
  }

  return (
    <div className="tabela-rolagem">
      <table>
        <thead>
          <tr>
            <th>id</th>
            <th>Título</th>
            <th>Solicitante</th>
            <th>Descrição</th>
            <th>Prioridade</th>
            <th>Status</th>
            <th>Aberto em</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {chamados.map((chamado) => (
            <tr key={chamado.id}>
              <td>{chamado.id}</td>
              <td title={chamado.descricao}>{chamado.titulo}</td>
              <td>{chamado.solicitante}</td>
              <td>{chamado.descricao}</td>
              <td>
                <span className={`etiqueta prioridade-${chamado.prioridade}`}>
                  {ROTULO_PRIORIDADE[chamado.prioridade]}
                </span>
              </td>
              <td>
                <span className={`etiqueta status-${chamado.status}`}>
                  {ROTULO_STATUS[chamado.status]}
                </span>
              </td>
              <td>{new Date(chamado.criado_em).toLocaleString('pt-BR')}</td>
              <td className="acoes-linha">
                <button className="secundario" onClick={() => onEditar(chamado)}>
                  Editar
                </button>
                <button className="perigo" onClick={() => onExcluir(chamado)}>
                  Excluir
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
