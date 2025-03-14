// Funções, Procedimentos e Métodos

/* 
    Assinaturas de métodos
    -> Passagem de parâmetros e Retorno de valor

// Sem passagem de parâmetros e Sem retorno de valor
function somar(){
    // Entrada
    let n1 = 10
    let n2 = 20
    // Processamento
    let r = n1 + n2
    // Saída
    console.log(`Resultado: ${r}`)
}
// Execução/Chamada da função
somar()


// Com passagem de parâmetros e Sem retorno de valor
function subtrair(n1, n2){
    // Processamento
    let r = n1 - n2
    // Saída
    console.log(`Resultado: ${r}`)
}
// Execução/Chamada da função
// Entrada
let num1 = 10
let num2 = 20
subtrair(num1, num2)


// Sem passagem de parâmetros e Comm retorno de valor
function multiplicar(){
    // Entrada
    let n1 = 10
    let n2 = 20
    // Processamento
    let r = n1 * n2
    return r
}
// Execução/Chamada da função
// Saída
console.log(`Resultado: ${multiplicar()}`)


// Com passagem de parâmetros e Com retorno de valor
function dividir(n1, n2){
    // Processamento
    return n1 / n2
}
// Execução/Chamada da função
// Entrada
num1 = 10
num2 = 20
// Saída
console.log(`Resultado: ${dividir(num1, num2)}`)
*/


// Literal
console.log('-> Função literal')

function somar(n1, n2){
    return n1 + n2
}
console.log( somar(10,20) )

console.log('\n')


// Função anônima (armazenada em uma variável)
console.log('-> Função anônima')

const subtrair = function(n1, n2){
    return n1 - n2
}
console.log( subtrair(40,30) )

console.log('\n')


// Os parâmetros são opcionais e pré-definidos
console.log('-> Parâmetros são opcionais e pré-definidos')

function somarVarios(n1, n2, n3 = 0, n4 = 10){
    return n1 + n2 + n3 + n4
}

console.log( somarVarios(2, 4, 6, 8, 10) )
console.log( somarVarios(2, 4, 6, 8) )
console.log( somarVarios(2, 4, 6) )
console.log( somarVarios(2, 4) )
console.log('\n')


// Função por parâmetro
console.log('-> Funções por parâmetro')

function apresentarResultado(n1, n2, operacao = somar){
    console.log( operacao(n1, n2) )
}

apresentarResultado(10, 20)
apresentarResultado(10, 20, subtrair)
apresentarResultado(10, 20, function(n1, n2){
    return n1 * n2
})
apresentarResultado(10, 20, (n1, n2) => n1 / n2)

console.log('\n')


console.log('-> Arrow Function')

// Literal
function dividirLiteral(n1, n2){
    return n1 / n2
}

//Anônima
const dividirAnonima = function (n1, n2){
    return n1 / n2
}

//Arrow function (com corpo uso de chaves para mais de uma linha de instrução)
const dividirArrowComCorpo = (n1, n2) => {
    return n1 / n2
}

// Arraw function (com uma linha de instrução)
const dividirArrow = (n1, n2) => n1 / n2

console.log(dividirArrow(9, 2))


// Arrow function sem parâmetros
function textoLiteral(){
    return 'String de retorno da função literal'
}

const textoArrow = () => 'String de retorno da Arrow function'

console.log(textoLiteral())
console.log(textoArrow())

console.log('\n')




// Closures
console.log('-> Funções Closures')

const externa = function(nome){

    let sobrenome = ' da Silva' // variável da função externa

    const interna = function(){
        return `Olá! ${nome} ${sobrenome}, seja bem-vindo!` // a função interna tem acesso ao parâmetro e a variável da função externa
    }

    return interna // nesse exemplo, a função externa retorna a função interna (na verdade, seu retorno)
}, 
nomeCompleto = externa('José')

console.log( nomeCompleto() )

// Este recurso possibilita a estrutura de componentes funcionais (equivalentes a classes em Orientação a Objetos)
