// Leia salário e idade. O empréstimo pode ser aprovado se: salário >= 3000 E idade >= 21.
programa {
  funcao inicio() {

    inteiro salario, idade

    escreva("Digite o seu salario?: ")
    leia(salario)

    escreva("Digite sua idade?: ")
    leia(idade)

    se(salario >= 3000 e idade >=21){
      escreva("O empréstimo pode ser aprovada.")
    } senao{
      escreva("O empréstimo não pode ser aprovado.")
    }
  }
}