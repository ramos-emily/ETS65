import estilos from './Fundamentos.module.css'
import {Botao} from '../componentes/Botao'
import { Contador } from '../componentes/Contador'

export function Fundamentos(){

    const mensagem = (texto) => alert(`Mensagem: ${texto}`)

    return(
        <div className={estilos.container}>
            <p className={estilos.titulo}>Fundamentos</p>

            <p className={estilos.subTitulo}>props</p>
        
            <div className={estilos.containerBotoes}>
                
                <Botao
                    titulo='blablabla' 
                    acao={() => mensagem('blablabla')}
                />
                <Botao
                    titulo='blablabla' 
                    acao={() => mensagem('aaaaaaaaa')}
                />
                <Botao
                    titulo='blablabla' 
                    acao={() => mensagem('seila')}
                />
            </div>

            <p className={estilos.subTitulo}>props</p>
            <Contador/>
            
        </div>
        
    )
}

