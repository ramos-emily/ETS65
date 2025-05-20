import styles from './Inicial.module.css';
import { Cabecalho } from '../componentes/Cabecalho';
import { Lateral } from '../componentes/Lateral';
import { Principal } from '../componentes/Principal';
import { Rodape } from '../componentes/Rodape';
import { useState } from 'react';

export function Inicial() {
  const [secaoAtiva, setSecaoAtiva] = useState("professor");

  return (
    <div className={styles.gridConteiner}>
      <Cabecalho />
      <Lateral onSelecionarSecao={setSecaoAtiva} />
      <Principal secao={secaoAtiva} />
      <Rodape />
    </div>
  );
}
