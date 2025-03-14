/*
Função síncrona -> Espera a tarefa acabar para executar a próxima tarefa
Função assíncrona -> Vai para a execução da próxima tarefa enquanto a tarefa atual é executada em "segundo plano".
                     Quando a tarefa é finalizada ela entra na "fila de tarefas" (task queue)

Vantagens:
    - Carregamento em segundo plano (não trava o site)
    - Execução ao termino (funções callback)
    - Requisições ao servidor (sem necessidade de recarregar a pagina)


Event Loop (modelo de concorrência): coordena eventos, interações do usuário, scripts, renderizações etc. em repetições continuas.
- Microtasks (executadas no loop atual)
- Macrotasks (executadas no próximo loop)
*/


console.log('-> Tarefas síncronas (executadas em ordem de execução/chamada) - Microtasks')
const funcao1 = () => console.log('Tarefa 01 (síncrona)')
const funcao2 = () => console.log('Tarefa 02 (síncrona)')
const funcao3 = () => console.log('Tarefa 03 (síncrona)')
// Chamadas das funções
/*
funcao1()
funcao2()
funcao3()
console.log('\n')
*/


// console.log('-> Exemplo de funções "auto-executaveis"')
// Auto-executável
/*
;( () => console.log('Tarefa 01 (síncrona)') )()
;( () => console.log('Tarefa 02 (síncrona)') )()
;( () => console.log('Tarefa 03 (síncrona)') )()
console.log('\n')
*/


// console.log('-> Event Loop\n   Tarefas assíncronas (executadas em segundo plano) - Macrotasks')
// setTimeout espera um tempo determinado em milisegundos para executar a tarefa (zero equivale a execução imediata)
const funcao4 = () => setTimeout( () => console.log('Tarefa 04 (assíncrona)'), 0 )
const funcao5 = () => setTimeout( () => console.log('Tarefa 05 (assíncrona)'), 0 )


//console.log('Chamadas: funções 1, 4, 2, 5, 3 \nExecuções: funções 1, 2, 3, 4, 5')
/*
funcao1()
funcao4()
funcao2()
funcao5()
funcao3()
*/


/* 
    A partir daqui os testes começam a ficar confusos (misturados) no console.
    Comente as chamadas das funções acima e abaixo para testar o script por partes
*/



// console.log('-> Callback functions e execuções em "segundo plano"')

// Array de strings
const bandas = ["Black Sabbath", "Led Zeppelin"]

// função para inserção de um novo valor que será executada após 1 segundo
const inserir = (banda) => {
    setTimeout( 
        () => bandas.push(banda)    
    ,1000 )
}

// função que lista o conteúdo do array que será executado em 1 segundos
const listar = () => {
    setTimeout( 
        () => bandas.forEach(banda => console.log(banda))
    ,2000 )
}

// Chamadas das funções
/*
listar()
inserir("Judas Priest")
*/

// Inverter os tempos de espera para testar o callback


/* 
    Comente as chamadas das funções acima e abaixo para testar o script por partes
*/


// console.log('-> Promise')
// Estrutura
const promessa = teste => {
    return new Promise( (resolve, reject) => {
        if(teste){
            resolve('Sucesso!')
        }else{
            reject('Falha!')
        }
    })
}
/*
promessa(true)
   .then( retorno => console.log(retorno) )
   .catch( motivo => console.log(motivo) )
*/


/*
console.log('Chamadas: promessa, 1, 4, 2, 5, 3 \nExecuções: 1, 2, 3, promessa, 4, 5')
// 'Promises são Microtasks executadas no fim da fila'

promessa(false)
   .then( retorno => console.log(retorno) )
   .catch( motivo => console.log(motivo) )
funcao1()
funcao4()
funcao2()
funcao5()
funcao3()
*/




// console.log('-> Fetch (consumo da API ViaCEP para teste)')
/*
    http://viacep.com.br

    Direto no navegador (URL)
    http://viacep.com.br/ws/13036210/json/ (cep existente)
    http://viacep.com.br/ws/12345678/json/ (cep não encontrado)
    http://viacep.com.br/ws/123456789/json/ (quantidade de dígitos incorreto)
*/


/*
const funcaoCepFetch = () => {
    fetch('http://viacep.com.br/ws/13036210/json/')
    .then( retorno => console.log(retorno) )
    .catch( motivo => console.log(motivo) )
}
funcaoCepFetch()
*/


/*
const funcaoCepFetch = (cep) => {
    fetch(`http://viacep.com.br/ws/${cep}/json/`)
    .then( retornoFetch => console.log(retornoFetch) )
    .catch( erro => console.log(`Ops! Ocorreu um erro na consulta (${erro})`) )
}
funcaoCepFetch(13036210)
*/


/*
const funcaoCepFetch = (cep) => {
    fetch(`http://viacep.com.br/ws/${cep}/json/`)
    .then( retornoFetch => retornoFetch )
    .then( retornoJSON => console.log( retornoJSON.json() ) )
    .catch( erro => console.log(`Ops! Ocorreu um erro na consulta (${erro})`) )
}
funcaoCepFetch(13036210)
// funcaoCepFetch(12345678)
// funcaoCepFetch(123456789)
*/


/*
const funcaoCepFetch = (cep) => {
    fetch(`http://viacep.com.br/ws/${cep}/json/`)
    .then( retornoFetch => retornoFetch )
    .then( retornoJSON => retornoJSON.json() )
    .then( endereco => { console.log(`Rua: ${endereco.logradouro}`)
                         console.log(`Bairro: ${endereco.bairro}`)
                         console.log(`Cidade: ${endereco.localidade}`) } )
    .catch( erro => console.log(`Ops! Ocorreu um erro na consulta (${erro})`) )
}
funcaoCepFetch(13036210)
// funcaoCepFetch(12345678)
// funcaoCepFetch(123456789)
*/


/*
const funcaoCepFetch = (cep) => {
    fetch(`http://viacep.com.br/ws/${cep}/json/`)
    .then( retornoFetch => retornoFetch )
    .then( retornoJSON => retornoJSON.json() )
    .then( endereco => { if (endereco.logradouro !== undefined) {
                            console.log(`Rua: ${endereco.logradouro}`)
                            console.log(`Bairro: ${endereco.bairro}`)
                            console.log(`Cidade: ${endereco.localidade}`) 
                         } else {
                            console.log(`CEP não localizado!`) 
                         } } )

    .catch( erro => console.log(`Ops! Ocorreu um erro na consulta (${erro})`) )
}
funcaoCepFetch(13036210)
// funcaoCepFetch(12345678)
// funcaoCepFetch(123456789)
*/



// console.log('-> Async-Await (consumo da API ViaCEP para teste)')

/*
const funcaoCepAsyncAwait = (cep) => {
    const retornoFetch = fetch(`http://viacep.com.br/ws/${cep}/json/`)
    console.log(retornoFetch)
}
funcaoCepAsyncAwait(13036210)
*/


/*
// Erro na conversão do objeto retornoFetch para JSON (linha 231)
// O objeto não existe nessa linha porque o fetch não foi concluído (na linha 230)

const funcaoCepAsyncAwait = (cep) => {
    const retornoFetch = fetch(`http://viacep.com.br/ws/${cep}/json/`)
    const retornoJSON = retornoFetch.json()
    console.log(retornoJSON)
}
funcaoCepAsyncAwait(13036210)
*/


/*
// O acrescimo do Async-Await faz com que o erro de conversão não ocorra
// Porém, ainda não é possível apresentar o objeto retornoJSON (linha 246) 
// porque é necessário esperar o fim da conversão (na linha 245)

const funcaoCepAsyncAwait = async (cep) => {
    const retornoFetch = await fetch(`http://viacep.com.br/ws/${cep}/json/`)
    const retornoJSON = retornoFetch.json()
    console.log(retornoJSON)
}
funcaoCepAsyncAwait(13036210)
*/


/*
const funcaoCepAsyncAwait = async (cep) => {
    const retornoFetch = await fetch(`http://viacep.com.br/ws/${cep}/json/`)
    const retornoJSON = await retornoFetch.json()
    console.log(retornoJSON)
}
funcaoCepAsyncAwait(13036210)
*/


/*
const funcaoCepAsyncAwait = async (cep) => {
    const retornoFetch = await fetch(`http://viacep.com.br/ws/${cep}/json/`)
    const endereco = await retornoFetch.json()
    console.log(`Rua: ${endereco.logradouro}`)
    console.log(`Bairro: ${endereco.bairro}`)
    console.log(`Cidade: ${endereco.localidade}`)
}
funcaoCepAsyncAwait(13036210)
*/


/*
const funcaoCepAsyncAwait = async (cep) => {
    try {
        const retornoFetch = await fetch(`http://viacep.com.br/ws/${cep}/json/`)
        const endereco = await retornoFetch.json()

        if (endereco.logradouro !== undefined) {
            console.log(`Rua: ${endereco.logradouro}`)
            console.log(`Bairro: ${endereco.bairro}`)
            console.log(`Cidade: ${endereco.localidade}`) 
        } else {
            console.log(`CEP não localizado!`) 
        }   

    } catch (erro) {
        console.log(`Ops! Ocorreu um erro na consulta (${erro})`)
    }
}
funcaoCepAsyncAwait(13036210)
// funcaoCepAsyncAwait(12345678)
// funcaoCepAsyncAwait(123456789)
*/