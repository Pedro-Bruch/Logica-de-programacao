//Peça para o usuário inserir três notas e calcule a média. Exiba "Aprovado" se a média for maior ou igual a 7 e "Reprovado" caso contrário.
programa {
  funcao inicio() {
    
    real nota1, nota2, nota3, conta

    escreva("Digite a primeira nota: ")
    leia(nota1)
    escreva("Digite a segunda nota: ")
    leia(nota2)
    escreva("Digite a terceira nota: ")
    leia(nota3)

    conta = (nota1 + nota2 + nota3) / 3

    se (conta < 7){
      escreva("Reprovado.")
    } senao {
      escreva("Aprovado.")
    }
  }
}
