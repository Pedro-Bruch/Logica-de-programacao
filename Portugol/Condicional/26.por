//Solicite ao usuário a idade e verifique se ele pode ou não entrar em um evento:
//a.	Menor que 18 anos: "Não autorizado"
//b.	18 anos ou mais: "Autorizado"



programa {
  funcao inicio() {
    
    inteiro idade

    escreva("Digite sua idade: ")
    leia(idade)

    se (idade < 18){
      escreva("Não autorizado")
    } senao{
      escreva("Autorizado")
    }
  }
}
