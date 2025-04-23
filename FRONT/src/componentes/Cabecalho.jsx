import styles from './Cabecalho.module.css'

export function Cabecalho(){
    return(
        <header className={styles.conteiner}>
            <p className={styles.titulo}>Controle de ambientes</p>
        </header>
    )
}
