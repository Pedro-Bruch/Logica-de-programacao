//O usuário deve informar o valor de um produto e o programa deve retornar a categoria do produto de acordo com a tabela:
//a.	Menor que 50: "Econômico"
//b.	Entre 50 e 150: "Médio"
//c.	Maior que 150: "Premium"


programa {
  funcao inicio() {
    
    real valor

    escreva("Digite o valor do produto:")
    leia(valor)

    se(valor < 50){
      escreva("Seu produto é ecônomico")
    } senao{
      se (valor > 150){
        escreva("Seu produto é premium")
      } senao {
        escreva("Seu produto é médio")
      }
    }
  }
}
