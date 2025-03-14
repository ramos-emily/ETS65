// Manipulação básica de Arrays

let numeros = [10, 20, 30, 40, 50]

// Varreduras
console.log('Varredura com for..in (apresenta o indice)');
for (let indice in numeros) {
    console.log(indice)
}

console.log('Varredura com for..of (apresenta o valor)');
for (let valor of numeros) {
    console.log(valor)
}

console.log('Varredura com forEach (com funções callback)');
numeros.forEach(function (valor) {
	console.log(valor)
});
console.log('\n')
// Com Arrow Function
numeros.forEach(valor => console.log(valor))


// Manipulação de dados

console.log('\nInserção com push (no fim)');
// Inserir um valor no fim
numeros.push(60)
console.log(numeros)

console.log('\nInserção com unshift (no começo)');
// Inserir um valor no começo
numeros.unshift(0);
console.log(numeros)

console.log('\nExclusão com pop (do fim)');
// Remover um valor do fim
numeros.pop()
console.log(numeros)

console.log('\nExclusão com shift (do começo)');
// Remover um valor do começo
numeros.shift()
console.log(numeros)

// Inclusão, Alteração e Exclusão em posições específicas do vetor

// Inclusão de mais valores para teste
console.log('\n')
numeros.push(70, 80, 90);
console.log(numeros)


console.log('\nInclusão com splice')
let indice = 5
let valoresRemovidos = 0
let novoValor = 60
numeros.splice(indice, valoresRemovidos, novoValor)
console.log(numeros)


console.log('\nAlteração com splice')
indice = 6
valoresRemovidos = 1
novoValor = 75
numeros.splice(indice, valoresRemovidos, novoValor)
console.log(numeros)


console.log('\Exclusão com splice')
indice = 5
valoresRemovidos = 4
numeros.splice(indice, valoresRemovidos, )
console.log(numeros)


// Consultas

console.log('\nFind (busca pelo número 30)');
// Busca um valor no array
numeros.find(function (valor, indice) {
        console.log(valor == 30);
});

console.log('\n')
// Retorna o valor se encontrado 
let busca = numeros.find((valor, indice) => valor == 30)
console.log(busca);

// Retorna undefined se o valor não for encontrado 
busca = numeros.find((valor, indice) => valor == 70)
console.log(busca);

// Busca um indice no array
busca = numeros.find((valor, indice) => indice == 4)
console.log(busca);

console.log('\nIndexOf (retorna o indice de um valor no array)');
// Retornar o indice da busca
console.log(numeros.indexOf(30));

// Retornar o -1 se não encontrado
console.log(numeros.indexOf(75));


// map 
/* retorna um novo array com os dados de um array origem transformado 
   (sempre com o mesmo tamanho) */
console.log('\nmap')
console.log('(transformação dos valores de array gerando um novo array de mesmo tamanho)')

let resultado = numeros.map(n => n * 2)
console.log(numeros)
console.log(resultado)
console.log('\n')

const dobro = n => n * 2
const mais10 =  n => n + 10
// Template String
const formataReal = n => `R$ ${parseFloat(n).toFixed(2).replace('.',',')}`

let resultado1 = numeros.map(dobro).map(mais10).map(formataReal)
console.log(numeros)
console.log(resultado1)


// filter
/* Recebe uma função callback que retorna true ou false
   true vai para o novo array false não */
console.log('\nfilter (filtrar valores)')

let menores = numeros.filter(n => n < 25)
console.log(numeros)
console.log(menores)


// reduce
/* Recebe uma função callback e (opcionalmente) um valor inicial 
   (se não for informado começa com o valor do índice zero) */
console.log('\nreduce (transforma os valores de um array em um único valor)')

let numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// sem valor inicial
console.log('\nSomatória')
const somatoria = numeros1.reduce((acumulador, atual) => {
    console.log(acumulador, atual)
    return acumulador + atual
})
console.log(somatoria)

// com valor inicial
console.log('\nSomatória com valor inicial 100')
const somatoria1 = numeros1.reduce((acumulador, atual) => {
    console.log(acumulador, atual)
    return acumulador + atual
}, 100)
console.log(somatoria1)



// Funções Callback
console.log('-> Funções Callback')

// Exemplo forEach
console.log('\nCallback: Exemplo forEach')

const bandas = ['Black Sabbath', 'Led Zeppelin', 'Judas Priest']

function mostrar(nome, indice){
    console.log(`${indice + 1} - ${nome}`)
}

bandas.forEach(mostrar)
console.log('\n')

bandas.forEach((nome, indice) => console.log(`${indice + 1}. ${nome}`))
console.log('\n')

bandas.forEach(nome => console.log(nome))


// Exemplo filter
console.log('\nCallback: Exemplo filter')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Forma 'tradicional'
const pares1 = []
for(let n of numeros){
    if(n % 2 == 0){
        pares1.push(n)
    }
}
console.log(numeros)
console.log(pares1)
console.log('\n')


// Com filter
// Callback de função anônima 
const pares2 = numeros.filter(function(n){
    return n % 2 == 0
})
console.log(pares2)
console.log('\n')


// Callback de Arrow Function
const impares = numeros.filter(n => n % 2 != 0)
console.log(impares)
console.log('\n')


// Atribuindo Arrows Functions a variáveis 
const filtraPares = n => n % 2 == 0
const filtraImpares = n => n % 2 != 0

const pares3 = numeros.filter(filtraPares)
const impares1 = numeros.filter(filtraImpares)

console.log(numeros)
console.log(pares3)
console.log(impares1)
console.log('\n')


// Concatenação
console.log('\nconcat')

const carros = ['fusca', 'brasilia', '147']
const motos = ['CG 125', 'Turuna', 'TT']
const ferroVelho = carros.concat(motos, 'mobilete')

console.log(carros)
console.log(motos)
console.log(ferroVelho)

console.log( [].concat(1,3,5.7,"João", true) )


// Desestruturação (destructuring)
console.log('\ndesestruturação')

let [a, b, c, d, e] = numeros

console.log(a)
console.log(b)
console.log(c)
console.log(d)
console.log(e)
console.log('\n')

let [x, y, z] = [a, b, c, d, e]

console.log(x)
console.log(y)
console.log(z)
console.log('\n')

let [n1, , n3] = [a, b, c, d, e]

console.log(n1)
console.log(n3)


// Operador ... é chamado de rest quando "agrupa" e spread quando "espalha"

// rest: agrupa vários valores passados por parametro em um array 
console.log('\nrest')

function adicao(...numeros){
    return numeros.reduce((total, numero) => total += numero)
}
console.log(adicao(2, 4, 6, 8))


// spread: Espalha os valores contidos em numeros para cada posição de numeros2 
//         e acrescenta os demais valores a partir da última posição ocupada 
console.log('\nspread')

const numeros2 = [...numeros, 60, 70, 80, 90]
console.log(numeros2)

// Sem o spread considera o array numeros e não seus valores separadamente
const numeros3 = [numeros, 60, 70, 80, 90]
console.log(numeros3)