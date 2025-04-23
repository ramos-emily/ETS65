import styles from './Botao.module.css'

export function Botao({titulo, acao}){
    return(
        <div 
            className={styles.conteiner}
            onClick={acao}
        >
            <p className={styles.texto}>{titulo}</p>
        </div>
    )
}
