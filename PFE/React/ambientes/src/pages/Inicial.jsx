import estilos from './Inicial.module.css'

export function Inicial(){
    return(
        <div className={estilos.gridConteiner}>
            <header className={estilos.cabecalho}>cabecalho</header>
            <aside className={estilos.lateral}>lateral</aside>
            <main className={estilos.principal}>principal</main>
            <footer className={estilos.rodape}>rodape</footer>
        </div>
    )
}