import estilos from './Inicial.module.css'
import { Cabecalho } from '../componentes/Cabecalho'
import { Lateral } from '../componentes/Lateral'
import { Principal } from '../componentes/Principal'
import { Rodape } from '../componentes/Rodape'

export function Inicial(){
    return(
        <div className={estilos.gridConteiner}>

            <Cabecalho />
            <Lateral />
            <Principal />
            <Rodape />
        </div>
    )
}