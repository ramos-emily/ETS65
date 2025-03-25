import estilos from './Login.module.css'

export function Login(){
    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Login veir</p>

            <form className={estilos.formulario}>

                <input placeholder='E-mail' className={estilos.campo} />
                <input placeholder='Senha' className={estilos.campo} />

                <button className={estilos.botao}>Entrar</button>

            </form>

        </div>
    )
}