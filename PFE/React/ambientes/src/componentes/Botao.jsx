import estilos from './Botao.module.css'

export function Botao ({titulo, acao}){
    
    
    return(
        <div
         className={estilos.conteiner}
         onClick={acao}
        >
            <p className={estilos.texto}>{titulo}</p>
        </div>
    )
}