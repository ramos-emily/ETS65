import styles from "./Principal.module.css";

export function Principal({ secao }) {
  function handleSubmit(e) {
    e.preventDefault();
    const data = new FormData(e.target);
    const formObject = Object.fromEntries(data.entries());
    console.log(formObject);
    alert("Formulário enviado com sucesso!");
  }

  return (
    <main className={styles.conteudo}>
      {secao === "professor" && (
        <form className={styles.formulario} onSubmit={handleSubmit}>
          <h2 className={styles.titulo}>Cadastro de Professor</h2>
          <input name="ni" placeholder="NI" />
          <input name="nome" placeholder="Nome" />
          <input name="email" placeholder="Email" />
          <input name="telefone" placeholder="Telefone" />
          <input name="nascimento" placeholder="Data de Nascimento" type="date" />
          <input name="contratacao" placeholder="Data de Contratação" type="date" />
          <input name="disciplinas" placeholder="Disciplinas" />
          <button type="submit">Confirmar</button>
        </form>
      )}

      {secao === "disciplina" && (
        <form className={styles.formulario} onSubmit={handleSubmit}>
          <h2 className={styles.titulo}>Cadastro de Disciplina</h2>
          <input name="nome" placeholder="Nome" />
          <input name="curso" placeholder="Curso" />
          <input name="cargaHoraria" placeholder="Carga Horária" type="number" />
          <input name="descricao" placeholder="Descrição" />
          <input name="professor" placeholder="Professor" />
          <button type="submit">Confirmar</button>
        </form>
      )}

      {secao === "ambiente" && (
        <form className={styles.formulario} onSubmit={handleSubmit}>
          <h2 className={styles.titulo}>Reserva de Ambiente</h2>
          <input name="dataInicio" placeholder="Data de Início" type="date" />
          <input name="dataTermino" placeholder="Data de Término" type="date" />
          <select name="periodo">
            <option value="">Selecione o Período</option>
            <option value="manha">Manhã</option>
            <option value="tarde">Tarde</option>
            <option value="noite">Noite</option>
          </select>
          <input name="sala" placeholder="Sala" />
          <input name="professor" placeholder="Professor" />
          <input name="disciplina" placeholder="Disciplina" />
          <button type="submit">Reservar</button>
        </form>
      )}

      {secao === "agendamento" && (
        <form className={styles.formulario} onSubmit={handleSubmit}>
          <h2 className={styles.titulo}>Sala</h2>
          <input name="Descrição" placeholder="Descrição" />
          <input name="Localização" placeholder="Localização" />
          <button type="submit">Confirmar</button>
        </form>
      )}
    </main>
  );
}
