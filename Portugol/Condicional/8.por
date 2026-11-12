//Faça um programa que permita o cadastro de produtos em uma empresa. O usuário deve informar o tipo de produto (Alimento, Bebida, Vestuário). 
//O programa deve exibir uma mensagem de confirmação com o tipo de produto cadastrado e se ele é perecível ou não, de acordo com as seguintes regras:
//Alimento: Perecível. Bebida: Não Perecível. Vestuário: Não Perecível
programa {
  funcao inicio() {

    inteiro perecivel

    escreva("Digite o tipo de produto \n1-Alimento\n2-Bebida\n3-Vestuário\n")
    leia(perecivel)

    se (perecivel == 1){
      escreva("Seu produto cadastrado foi Alimento.\nEle é Perecível!")
    } senao se (perecivel == 2){
      escreva("Seu produto cadastrado foi Bebida.\nEle não é Perecível")
    } senao {
      escreva("Seu produto cadastrado foi Vestuário.\nEle nao é Perecível")
    }
  }
}
