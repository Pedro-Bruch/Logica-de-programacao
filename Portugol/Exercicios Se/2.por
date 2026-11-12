// Leia a idade. Informe se a pessoa é "Maior de idade" ou "Menor de idade".
programa {
  funcao inicio() {
    inteiro idade
    escreva("Digite sua idade: ")
    leia(idade)
    se(idade >= 18) {
      escreva("Você é maior de idade.")
    } senao {
      escreva("Você é menor de idade.")
    }    
  }
}
