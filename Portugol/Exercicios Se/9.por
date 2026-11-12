//9.Entrada no cinema
//Leia idade e se a pessoa está acompanhada.
//A entrada é permitida se:
//idade >= 18 OU
//idade >= 16 E estiver acompanhada.
programa {
  funcao inicio() {

    inteiro idade, acompanhada, idadeAcompanhada

    escreva("Qual sua idade?: ")
    leia(idade) 

    se (idade >= 18){
      escreva("A entrada é liberada.")
    }senao{

      escreva("Ela esta acompanhada?\n1-Sim\n2-Não\n")
      leia(acompanhada)

      escreva("Qual a idade do acompanhante?")
      leia(idadeAcompanhada)

      se(idadeAcompanhada >= 18){
    se(idade >= 16 e acompanhada == 1){
      escreva("A entrada é liberada.")
    }senao{
      escreva("A entrada nao é liberada.")
    }} senao{
      escreva("A entrada nao é liberada.")}}
  }
}