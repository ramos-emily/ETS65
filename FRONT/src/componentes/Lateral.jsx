// src/componentes/Lateral.jsx
import styles from "./Lateral.module.css";
import { PiStudentBold } from "react-icons/pi";
import { FaPencilAlt, FaCalendarAlt, FaEnvira } from "react-icons/fa";
import foto from "../assets/usuario.png";

export function Lateral({ onSelecionarSecao }) {
  return (
    <aside className={styles.conteiner}>
      <header>
        <img
          className={styles.imagemCabecalho}
          src="https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg"
        />
        <div className={styles.conteinerUsuario}>
          <img className={styles.fotoUsuario} src={foto} />
          <p className={styles.nomeUsuario}>Emis</p>
        </div>
      </header>

      <section className={styles.conteinerBotoes}>
        <div className={styles.botao} onClick={() => onSelecionarSecao("professor")}>
          <PiStudentBold className={styles.icone} />
          Professor
        </div>

        <div className={styles.botao} onClick={() => onSelecionarSecao("disciplina")}>
          <FaPencilAlt className={styles.icone} />
          Disciplina
        </div>

        <div className={styles.botao} onClick={() => onSelecionarSecao("ambiente")}>
          <FaEnvira className={styles.icone} />
          Ambiente
        </div>

        <div className={styles.botao} onClick={() => onSelecionarSecao("agendamento")}>
          <FaCalendarAlt className={styles.icone} />
          Agendamento
        </div>
      </section>
    </aside>
  );
}
