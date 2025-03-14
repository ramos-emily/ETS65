import estilos from './Fundamentos.module.css'
import {Botao} from '../componentes/Botao'

export function Fundamentos(){

    const mensagem = (texto) => alert(`Mensagem: ${texto}`)

    return(
        <div className={estilos.container}>
            <p className={estilos.titulo}>Fundamentos</p>
        
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
            
        </div>
        
    )
}

