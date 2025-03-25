import estilos from './Contador.module.css'
import {useState} from 'react'

export function Contador (){

    const [valor, SetValor] = useState(0)
    

    const somar = () => {
        SetValor(valor + 1)
        console.log(valor) 
    }

    const subtrair = () => {
        SetValor(valor - 1)
        console.log(valor) 
    }
    
    

    
    return (
        <div className={estilos.conteiner}>
            <p className={estilos.valor}>Contador</p>
            
            <div className={estilos.conteinerBotoes}>

                <div className={estilos.botao}
                ></div>

                <div className={estilos.subtrair}
                onClick={subtrair}
                >-</div>

                <p className={estilos.valor}>{valor}</p>

                <div className={estilos.somar}
                onClick={somar}
                >+</div>
            </div>   
        
        </div>
    )   
}