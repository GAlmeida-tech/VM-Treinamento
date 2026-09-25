import { useEffect, useState } from 'react'
import {
  atualizarChamado,
  criarChamado,
  excluirChamado,
  listarChamados,
  type Chamado,
  type DadosChamado,
} from './api/chamados'
import { FormularioChamado } from './components/FormularioChamado'
import { TabelaChamados } from './components/TabelaChamados'

function App() {
  const [chamados, setChamados] = useState<Chamado[]>([])
  const [emEdicao, setEmEdicao] = useState<Chamado | null>(null)
  const [carregando, setCarregando] = useState(true)
  const [salvando, setSalvando] = useState(false)
  const [erro, setErro] = useState<string | null>(null)

  // READ: carrega a lista ao abrir a tela
  useEffect(() => {
    listarChamados()
      .then(setChamados)
      .catch((e: Error) => setErro(e.message))
      .finally(() => setCarregando(false))
  }, [])

  // CREATE e UPDATE
  async function salvar(dados: DadosChamado) {
    setSalvando(true)
    setErro(null)
    try {
      if (emEdicao) {
        const atualizado = await atualizarChamado(emEdicao.id, dados)
        setChamados((lista) => lista.map((c) => (c.id === atualizado.id ? atualizado : c)))
        setEmEdicao(null)
      } else {
        const criado = await criarChamado(dados)
        setChamados((lista) => [...lista, criado])
      }
    } catch (e) {
      setErro((e as Error).message)
    } finally {
      setSalvando(false)
    }
  }

  // DELETE
  async function excluir(chamado: Chamado) {
    if (!confirm(`Excluir o chamado #${chamado.id} "${chamado.titulo}"?`)) return

    setErro(null)
    try {
      await excluirChamado(chamado.id)
      setChamados((lista) => lista.filter((c) => c.id !== chamado.id))
      if (emEdicao?.id === chamado.id) setEmEdicao(null)
    } catch (e) {
      setErro((e as Error).message)
    }
  }

  return (
    <main className="pagina">
      <h1>Chamados</h1>

      {erro && <p className="erro">{erro}</p>}

      <div className="conteudo">
        <FormularioChamado
          // A key força o formulário a recomeçar ao trocar de chamado
          key={emEdicao?.id ?? 'novo'}
          chamadoEmEdicao={emEdicao}
          salvando={salvando}
          onSalvar={salvar}
          onCancelar={() => setEmEdicao(null)}
        />

        <section>
          <h2>Lista</h2>
          {carregando ? (
            <p className="vazio">Carregando...</p>
          ) : (
            <TabelaChamados chamados={chamados} onEditar={setEmEdicao} onExcluir={excluir} />
          )}
        </section>
      </div>
    </main>
  )
}

export default App
