import estilos from './Contador.module.css'
import { useState } from 'react' //faz a renderização de variavel

export function Contador(){

    const[valor, setValor] = useState(0)

    const somar = () => {
        setValor(valor + 1) 
    }
    const subatrair= () => {
        setValor(valor - 1)
    }

    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Contador</p>
            <div className={estilos.conteinerBotoes}>
                <div
                 className={estilos.botao}
                 onClick={subatrair}
                >-</div>
                <p className={estilos.valor}>{valor}</p>
                <div
                className={estilos.botao}
                onClick={somar}
                >+</div>
        </div>
            
        </div>
        
    )
}