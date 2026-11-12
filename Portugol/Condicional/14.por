//Peça para o usuário inserir a idade e classifique como "Criança", "Adolescente", "Adulto" ou "Idoso", de acordo com os seguintes critérios:
//0 a 12 anos: Criança
//13 a 17 anos: Adolescente
//18 a 60 anos: Adulto
//Acima de 60 anos: Idoso
programa {
  funcao inicio() {
    
    inteiro idade

    escreva("Digite sua idade: ")
    leia(idade)

    se (idade >= 0 e idade <= 12){
      escreva("Você é criança.")
    } senao{
      se (idade >= 13 e idade <= 17){
        escreva("Você é adolescente.")
      } senao{
        se (idade >= 18 e idade <= 60){
          escreva("Você é adulto.")
        } senao {
          escreva("Você é idoso.")
        }
      }
    }
  }
}
