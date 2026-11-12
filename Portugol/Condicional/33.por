//33.	Ano de eleição
//Solicite o ano de nascimento de uma pessoa e verifique se ela já pode votar. A idade mínima para votar é 16 anos, mas a pessoa só é obrigada a votar a partir de 18 anos.


programa {
  funcao inicio() {
    
    inteiro data, idade

    escreva("Qual o ano da sua data de nascimento: ")
    leia(data)

    idade = 2026 - data
    se (idade >= 15 e idade <= 17){
      escreva("Você tem a idade mínima para votar.")
    } senao{
      se (idade >= 18){
        escreva("Você é obrigado a votar.")
      } senao{
        escreva("Você não tem idade suficiente para votar.")
      }
    }
  }
}
