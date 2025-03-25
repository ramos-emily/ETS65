console.log('-> Funções do objeto window')

console.log('Informações sobre o navegador')
console.log(window.navigator)
console.log('\n')

console.log('Informações sobre a tela')
console.log(window.screen)
console.log('\n')

console.log('Dimensões da tela (incluindo a barra de status)')
console.log(`Altura: ${window.outerHeight}`)
console.log(`Largura: ${window.outerWidth}`)
console.log('\n')

console.log('Dimensões internas da tela (excluindo a barra de status)')
console.log(`Altura: ${window.innerHeight}`)
console.log(`Largura: ${window.innerWidth}`)
console.log('\n')

console.log('Informações sobre o endereço acessado')
console.log(window.location)
console.log('\n')

window.onload = () => console.log('Função executada assim que o conteúdo da página foi carregado completamente')
console.log('\n')



console.log('-> Funções do objeto document')


// Métodos de seleção de elementos:
/*
// seleciona UM elemento a partir do seu ID exclusivo
document.getElementById(id)
// seleciona UM elemento a partir da sua classe (será selecionado o primeiro elemento encontrado da classe indicada)
document.getElementsByClassName(className)
// seleciona UM elemento a partir da sua tag. (será selecionado o primeiro elemento encontrado da tag indicada)
document.getElementsByTagName(tagName)
// seleciona UM elemento a partir de seletores CSS.
document.querySelector(cssSelector)
// retorna uma LISTA com todos os elementos encontrados pelo seletor css indicado
document.querySelectorAll(cssSelector)
*/

// Alguns métodos de manipulaçao de elementos:
/*
// Cria um novo elemento HTML.
createElement()
// Acrescenta um elemento a uma lista de elementos HTML (filhos) a partir de um elemento HTML pai indicado. 
appendChild()
// Obtém e/ou define o conteúdo de texto de um elemento HTML.  
textContent
// obtém e/ou define um elemento HTML. 
innerHTML
// Acrescenta um elemento HTML após o último elemento filho a partir de um elemento HTML pai indicado. 
append() 
// Remove um elemento HTML filho a partir de um elemento HTML pai indicado. 
removeChild()
// Retorna o elemento HTML pai a partir de um elemento HTML filho indicado. 
parentNode() 
*/


console.log('Obtém o elemento HTML completo')
let elementoHTML = document.getElementById("exemplos")
console.log(elementoHTML)
console.log('\n')


console.log('Obtém o conteúdo (valor ente a abertura e o fechamento da tag) do elemento HTML')
let valorElementoHTML = document.getElementById("exemplos").textContent
console.log(valorElementoHTML)
console.log('\n')



console.log('Evento onClick')
// Vincula o evento onclick do botão a execução da arrow function
// Manipulação de propriedades de elementos HTML

let exemploLista = document.getElementById("exemplo-lista")
exemploLista.onclick = () => alert('Monta uma lista numerada com os nomes informados.')

let exemploCalculadora = document.getElementById("exemplo-calculadora")
exemploCalculadora.onclick = () => alert('Executa as quatro operações básicas com dois números informados.\nApresenta combinações de cores diferentes dependendo do resultado.')

// Clique sobre os titulos de cada exemplo (Lista e Calculadora) para executar as funções



// Manipulação de propriedades de elementos HTML e atributos CSS
let flag = true
let titulo = document.getElementById("exemplos")
titulo.onclick = () => { if (flag) {
                             titulo.innerHTML = "Titulo alterado pelo evento click" 
                             titulo.style.color = '#ffc300'
                             flag = false
                         } else {
                             titulo.innerHTML = "Integração do JS com HTML e CSS" 
                             titulo.style.color = '#aa9e9d'
                             flag = true
                         } }

// Clique sobre o titulo dos exemplos para executar a função

/*
    Obs.: As funções do objeto window que interagem com o usuario (alert, prompt, etc.) 
          não são recomendadas para aplicações reais (existem alternativas mais eficientes)
*/



/* Exemplo Lista */

// Obtém as referências dos elementos HTML
let nome = document.getElementById("nome")
let mensagem = document.getElementById("mensagem")
let lista = document.getElementById("lista")
let btnMensagem = document.getElementById("btn-mensagem")
// Vincula o evento click do botão a execução da função literal listar
btnMensagem.addEventListener("click", listar)


function listar() { 
    // Apresenta a mensagem
    mensagem.innerHTML = "Olá! " + nome.value

    // Cria um elemento HTML li e atribui na variável item
    let item = document.createElement("li")
    // Acrescenta o nome digitado no item
    item.innerHTML = nome.value
    // Insere o novo elemento item (li) como filho do elemento lista (ol) 
    // já existente no documento HTML
    lista.appendChild(item)
    // Limpa o input
    nome.value = ""
    // E posiciona o curso para a próxima inserção
    nome.focus()
}


/* Exemplo Calculadora */

let numero1 = document.getElementById("n1")
let numero2 = document.getElementById("n2")

let soma = document.getElementById("somar")
let subtracao = document.getElementById("subtrair")
let multiplicacao = document.getElementById("multiplicar")
let divisao = document.getElementById("dividir")
let resultado = document.getElementById("resultado")

let btnCalcular = document.getElementById("btn-calcular")
btnCalcular.addEventListener("click", calcular)

let btnLimpar = document.getElementById("btn-limpar")
btnLimpar.addEventListener("click", limpar)


function somar(num1, num2){
    return num1 + num2
}

function subtrair(num1, num2){
    return num1 - num2
}

function multiplicar(num1, num2){
    return num1 * num2
}

function dividir(num1, num2){
    return num1 / num2
}

function calcular() { 

    let n1, n2, r

    // se retornar false interrompe a execução da função
    if( !numeroValido(document.getElementById("n1")) ) { 
        return
    } else {
        n1 = numeroValido(document.getElementById("n1"))
    }

    if( !numeroValido(document.getElementById("n2")) ) {
        return
    } else {
        n2 = numeroValido(document.getElementById("n2"))
    }

    // if ternário encadeado
    r = soma.checked ? somar(n1, n2) : 
        subtracao.checked ? subtrair(n1, n2) :
        multiplicacao.checked ? multiplicar(n1, n2) :
        divisao.checked ? dividir(n1, n2) : null

    resultado.innerHTML = r
    cores(r)
}

function numeroValido(elemento){

    if ( elemento.value == "" || isNaN(elemento.value) ) {
        alert("Informe somente o números.")
        elemento.focus()
        return false
    } 
    
    if (elemento.value == 0) {
        alert("Informe números (positivos ou negativos) diferentes de zero.")
        elemento.focus()
        return false
    } 

    if (elemento.value < -10000 || elemento.value > 10000) {
        alert("Informe números com no máximo 4 digitos.")
        elemento.focus()
        return false
    } 

    return Number( elemento.value )
}

function limpar() {
    numero1.value = ""
    numero2.value = ""
    resultado.innerHTML = ""
    soma.checked = true
    resultado.style.color = "#000"
    resultado.style.background = "#fff"
    numero1.focus()
}


function cores(r){

    resultado.style.color = "#fff"

    r > 0 ? resultado.style.background = '#386641' : resultado.style.background = '#d90429'
}