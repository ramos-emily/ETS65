// Declaração de variáveis
let nome = 'Jão'
let notaFinal = 0.0
let recuperacao = 0.0
let frequencia = 0.0


console.log('-> Instrução Condicional Simples')

notaFinal = 7.5

if (notaFinal >= 6.0) {
    console.log(`O aluno ${nome} foi aprovado!`)
}

console.log('\n')
console.log('-> Instrução Condicional Composta')

notaFinal = 7.5

if (notaFinal >= 6.0) {
    console.log(`O aluno ${nome} foi aprovado!`)
} else {
    console.log(`O aluno ${nome} foi reprovado!`)
}


console.log('\n')
console.log('-> Operador ternário')

notaFinal = 5


//operador ternario: if igual o de antes
//voce atribui um valor, atravez de uma condição, se for vdd executa o 1 se nn o 2
let situacao = notaFinal >= 6.0 ? 'aprovado!' : 'reprovado!'

console.log(`O aluno ${nome} foi ${situacao}`)


console.log('\n')
console.log('-> Instrução Condicional Encadeada')

notaFinal = 3.5
recuperacao = 7.0

if (notaFinal >= 6.0) {
    console.log(`O aluno ${nome} foi aprovado!`)

} else if (recuperacao >= 6.0) {
    console.log(`O aluno ${nome} foi aprovado na recuperação!`)

} else {
    console.log(`O aluno ${nome} foi reprovado!`)
}


console.log('\n')
console.log('-> Instrução Multicondicional Encadeada')

notaFinal = 9.5
tcc = true
frequencia = 47.0
recuperacao = 0.0

if (frequencia < 50) {
    console.log(`O aluno ${nome} foi retido por faltas!`)

} else {

    if (notaFinal >= 6.0 && tcc) {
        console.log(`O aluno ${nome} foi aprovado!`)

    } else {

        if (recuperacao >= 6.0) {
            console.log(`O aluno ${nome} foi aprovado na recuperação!`)

        } else {
            console.log(`O aluno ${nome} foi reprovado!`)
        }
    }
}


console.log('\n')
console.log('-> Instrução Condicional Escolha..Caso')

console.log('Digite:')
console.log('1 - Para o nome do aluno')
console.log('2 - Para a nota final do aluno')
console.log('3 - Para a nota de recuperação do aluno')
console.log('4 - Para a frequencia do aluno')

let opcao = 2

switch (opcao) {

    case 1: //se talala
        console.log(`Nome: ${nome}`)    
        break    

    case 2:
        console.log(`Nota final: ${notaFinal}`)    
        break    

    case 3:
        console.log(`Nota recuperação: ${recuperacao}`)    
        break    

    case 4:
        console.log(`Frequencia: ${frequencia}`)    
        break    

    default: //else
        console.log('Opção inválida!')    
}