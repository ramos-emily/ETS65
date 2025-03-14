let soma = document.getElementById("somar")
let subtracao = document.getElementById("subtrair")
let multiplicacao = document.getElementById("multiplicar")
let divisao = document.getElementById("dividir")
let resultado = document.getElementById("resultado")

let btnCalcular = document.getElementById("btn-calcular")

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

btnCalcular.onclick =  () => {

    let n1, n2, r

    n1 = Number( document.getElementById("numero1").value )
    n2 = Number( document.getElementById("numero2").value )

    if(soma.checked){
        r = somar(n1, n2)
    }

    subtracao.checked ? r = subtrair(n1, n2) : null
    multiplicacao.checked ? r = multiplicar(n1, n2) : null
    divisao.checked ? r = dividir(n1, n2) : null

    resultado.innerHTML = `Resultado: ${r}`
}


