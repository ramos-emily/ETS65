/* 
    Convenção adotada: camelCase
    Aspas simples para delimitação de strings
    Ponto-e-virgula como fim de instrução é opcional (não utilizo)
    Entrada e saída: console.log() 
                     posteriormente integraremos com o HTML por meio do DOM
*/


// Declaração de variáveis
    var x        // Declara uma variável (inicialização opcional)
    let y        // Declara uma variável local de escopo do bloco (inicialização opcional)
    const z = 0  // Declara uma constante de escopo de bloco (inicialização obrigatória)


/*
    Tipos de dados (primitivos):
        -> string (textos, caracteres alfanuméricos)
        -> number (positivos, negativos, inteiros e reais)
        -> boolean (verdadeiro ou falso)
    
        -> null
        -> undefined

    Objeto
*/


console.log('-> Tipos de dados')

// typeof(): retorna o tipo de dado

var produto = 'Lápis'
var preco = 2.50
var disponivel = true
var ultimaCompra

console.log( typeof(produto) )
console.log( typeof(preco) )
console.log( typeof(disponivel) )
console.log( typeof(ultimaCompra) )
console.log('\n') // pula uma linha no console

ultimaCompra = new Date // Obtém a data do SO
console.log(ultimaCompra)
console.log( typeof(ultimaCompra) )
console.log('\n')

/* 
    Cuidado!
    Declarações duplicadas com var não dará erro

    Por isso, opte sempre por let (escopo de bloco) e, se necessário, mude para var
*/
var variavel = ''
var variavel = ''


/* 
    Atenção!
    JS tem tipagem de dados fraca (não há obrigatoriedade de conversão explícita)
*/
let n = 10
console.log( typeof(n) )
n = false // não dará erro
console.log( typeof(n) )
console.log('\n')


console.log('-> Converções de tipos')

/* 
    Atenção!
    Conversões de tipos implicitas
*/
n = '10'
console.log( typeof(n) )

console.log(n / 2) 
console.log(n * 2) 
console.log(n - 2) 
console.log(n + 2) // Concatenação
console.log('\n')

// Conversões de tipos explicitas

console.log( Number(n) + 2) // de string para number

let valor = 10
console.log( String(valor) + 2) // de number para string

//IMPORTANTE!!!
console.log('-> Concatenação e Template Literals (ou Template Strings)')

// Declaração de variáveis
let jantar, garcom, total

// Atribuindo valores iniciais
jantar = 100.00
garcom = jantar * 0.1
total = jantar + garcom

// Concatenação
console.log("Jantar: " + jantar + "\nGarçom: " + garcom + "\nTotal: " + total)

// Template Literals (ou Template Strings) utiliza crases como delimitadores e possibilita passagens de parâmetros
console.log(`Jantar: ${jantar} \nGarçom: ${garcom} \nTotal: ${total}`)
// sifrao e caracter de entrada de parametro


// Entrada e Saída de dados
/*
    Por enquanto, sugiro a utilização das funções prompt() e alert()
    respectivamente para entrada e saída.

    Essas funções não são as melhores alternativas e (em alguns casos são desaconselháveis), porém,
    nesse momento, auxiliarão na leitura e apresentação de dados
*/

console.log('-> Exemplo restaurante com as funções prompt() e alert()')

// Entrada prompty é a caixinha que aparece em cima da pagina (ELA LE TUDO COMO STRING!! PRECISA SER CONVERTIDA)
jantar = Number( prompt('Informe o valor do jantar') )

// Processamento
garcom = jantar * 0.1
total = jantar + garcom

// Saída
alert(`Jantar: ${jantar} \nGarçom: ${garcom} \nTotal: ${total}`)

