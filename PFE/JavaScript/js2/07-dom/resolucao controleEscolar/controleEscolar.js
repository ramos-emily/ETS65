/*
Desenvolva uma página web para o controle de alunos de uma escola 
a partir dos seguintes requisitos:
-> Leia o nome, nota final e frequência do aluno
   Obs.: A frequancia será lida como um número real, porém, considerada como uma porcentagem.
         Exemplo: 75.00 equivale a 75%
-> A frequência mínima para aprovação é de 75% (caso contrário o aluno estará reprovado).
-> A nota final mínima para aprovação é 6.0
-> Caso o aluno tenha frequência satisfatória e não atinja a nota mínima, será lida uma nota de recuperação
   que também deverá ser igual ou superior a 6.0
*/

let nome = document.getElementById("nome")
let nota = document.getElementById("nota")
let frequencia = document.getElementById("frequencia")
let recuperacaoLabel = document.getElementById("recuperacao-label")
let recuperacao = document.getElementById("recuperacao")
let mensagem = document.getElementById("mensagem")
let btnVerificar = document.getElementById("btn-verificar")

let rec = false

btnVerificar.onclick = () => { 

   if (frequencia.value < 75) {
      mensagem.innerHTML = "Reprovado por frequência"

   } else {

      if (!rec && nota.value >= 6.0) {
         mensagem.innerHTML = "Aprovado"
      } 
  
      if (rec && recuperacao.value >= 6.0 ) {
         mensagem.innerHTML = "Aprovado na recuperação"
      }

      if (rec && recuperacao.value < 6.0 ) {
         mensagem.innerHTML = "Reprovado"
      }

      if (!rec && nota.value < 6.0) {
         habilitaRecuperacao()
      }
   }
}


let habilitaRecuperacao = () => {

   recuperacaoLabel.removeAttribute("hidden")
   recuperacao.removeAttribute("hidden")
   recuperacao.focus()

   nome.disabled = true
   nome.style.color = '#fff'

   nota.disabled = true
   nota.style.color = '#fff'

   frequencia.disabled = true
   frequencia.style.color = '#fff'

   btnVerificar.innerHTML = "Verificar recuperação"
   mensagem.innerHTML = "Informe a nota de recuperação"

   rec = true
}