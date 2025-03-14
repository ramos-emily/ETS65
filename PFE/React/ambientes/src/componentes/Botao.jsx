import estilos from './Botao.module.css'

export function Botao({titulo,acao}){
    return(
        <div 
            onClick={acao}
            className={estilos.container}
        >
            <p className={estilos.texto}>{titulo}</p>
            
        </div>
    )
}