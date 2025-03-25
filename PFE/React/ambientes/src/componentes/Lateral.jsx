import estilos from './Lateral.module.css'
import foto from '../assets/sherk.png'
import { PiStudentDuotone } from "react-icons/pi";
import { LiaSchoolSolid } from "react-icons/lia";
import { TfiAgenda } from "react-icons/tfi";
import { SiGoogleclassroom } from "react-icons/si";


export function Lateral(){
    return(
        <aside className={estilos.conteiner}>

            <header>
{/* 
                <img 
                    className={estilos.imagemCabecalho}  
                    // src='https://images.unsplash.com/photo-1610054178419-6f29163251d7?q=80&w=1287&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
                /> */}

                <div className={estilos.conteinerUsuario}>
                    <img 
                        className={estilos.fotoUsuario} 
                        src={foto}
                    />
                    
                </div>

            </header>
            
            <section className={estilos.conteinerBotoes}>
                <div 
                    className={estilos.botao}><PiStudentDuotone size={20} />Professor
                </div>
                <div 
                    className={estilos.botao}><LiaSchoolSolid size={20} />Disciplina</div>
                <div 
                    className={estilos.botao}><SiGoogleclassroom size={20}/>Ambiente
                </div>
                <div 
                    className={estilos.botao}><TfiAgenda size={15} />Agendamento
                </div>
            </section>


        </aside>
    )
}