import styles from './Contador.module.css'
import {useState} from 'react'

export function Contador(){

    const [valor, setValor] = useState(0)

    const somar = () => {
        setValor(valor + 1)
    }

    const subtrair = () => {
        setValor(valor - 1)
    }

    return(
        <div className={styles.conteiner}>

            <p className={styles.titulo}>Contador</p>

            <div className={styles.conteinerBotoes}>

                <div 
                    className={styles.botao} 
                    onClick={subtrair}
                >-</div>

                <p className={styles.valor}>{valor}</p>

                <div 
                    className={styles.botao}
                    onClick={somar}
                >+</div>
            </div>

        </div>
    )
}
