// Declaração de variáveis
let limite
let contador
let resposta


console.log('-> Laços de repetição com pré-teste (while)')

limite = 10
contador = 1

while (contador <= limite) {
    console.log(`${contador}º iteração`)
    contador++
}


contador = 20
while (contador <= limite) { // Não entra no laço
    console.log(`${contador}º iteração`)
    contador++
}


console.log('\n')
console.log('Laços de repetição com pós-teste (do..while)')

limite = 10
contador = 1

do {
    console.log(`${contador}º iteração`)
    contador++
} while (contador <= limite)


console.log('\n')
contador = 20
do {
    console.log(`${contador}º iteração`)
    contador++
} while (contador <= limite) // Quando testa a primeira iteração já aconteceu


console.log('\n')
console.log('Laços de repetição incondicional (for)')

limite = 10

for (contador = 1; contador <= limite; contador++) {
    console.log(`${contador}º iteração`)
}


console.log('\n')
limite = 1

for (contador = 10; contador >= limite; contador--) {
    console.log(`${contador}º iteração`)
}


console.log('\n')
limite = 10

for (contador = 2; contador <= limite; contador += 2) {
    console.log(contador)
}


console.log('\n')
console.log('Laços de repetição incondicional (for)')
console.log('Exemplo Tabuada')

let tabuada = 7

for (let i = 1; i <= 10; i++) {

    console.log(`${tabuada} X ${i} = ${(tabuada * i)}`)
}


console.log('\n')
console.log('Laços de repetição seletivo (break)')

limite = 10

contador = 1

while (true) {
    console.log(`${contador}º iteração`)
    contador++

    if (contador > limite) {
        console.log('Iterações interrompidas pelo break...')
        break
    }
}


console.log('\n')
contador = 1

do {
    console.log(`${contador}º iteração`)
    contador++

    if (contador > limite) {
        console.log('Iterações interrompidas pelo break...')
        break
    }
} while (true)


console.log('\n')
console.log('Laços de repetição seletivo (break)')
console.log('Somatória de números')

contador = 1
somatoria = 0
let numero = 10

while (true) {
    
    somatoria += contador
    contador++

    if (contador > numero) {
        console.log(`A soma dos números entre 1 e ${numero} é ${somatoria}`)
        break
    }
}


console.log('\n')
console.log('Somente números impares (continue)')

contador = 1

do {

    if (contador % 2 == 0){
        contador++
        continue
    }

    if (contador > limite) {
        console.log('Iterações interrompidas pelo break...')
        break
    }

    console.log(`${contador}º iteração`)
    contador++
    
} while (true)