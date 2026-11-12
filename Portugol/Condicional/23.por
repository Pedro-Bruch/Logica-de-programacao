//23.	Classificar notas
//Peça para o usuário inserir uma nota e, de acordo com a nota, classifique como:
//a.	0 a 4: "Reprovado"
//b.	5 a 6: "Recuperação"
//c.	7 a 10: "Aprovado"


programa {
  funcao inicio() {
    
    inteiro nota

    escreva("Digite a nota: ")
    leia(nota)

    se (nota <= 4){
      escreva("Reprovado")
    } senao{
      se (nota >= 5 e nota <=6){
        escreva("Recuperação")
      } senao{
        escreva("Aprovado")
      }
    }
  }
}
