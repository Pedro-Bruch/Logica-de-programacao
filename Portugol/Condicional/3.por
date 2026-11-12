//Fazer um algoritmo para imprimir o conceito de um aluno, dada a sua nota. 
//Supor notas inteiras somente. O critério para conceitos o seguinte:   
//nota inferiores a 3 - conceito E   nota de 3 a 5 - conceito D   notas 6 e 7 - conceito C   
//notas 8 e 9 - conceito B   nota 10 - conceito A   

programa {
  funcao inicio() {

    inteiro nota

    escreva("Escreva a nota do aluno: ")
    leia(nota)

    se (nota >= 0 e nota < 3){
      escreva("O conceito do aluno é: E")
    } senao{
      se (nota >= 3 e nota <= 5){
        escreva("O conceito do aluno é: D")
      }senao{
        se (nota == 6 ou nota == 7){
          escreva("O conceito do aluno é: C")
        } senao{
          se (nota == 8 ou nota == 9){
            escreva("O conceito do aluno é: B")
          } senao{
            escreva("O conceito do aluno é: A")
          }
        }
      }
    }
  }
}
