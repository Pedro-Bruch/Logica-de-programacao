//7.Desenvolva um programa que analise o desempenho de vendas de uma loja. 
//O usuário deve informar o total de vendas em um mês. Com base no valor, o programa deve classificar o desempenho de vendas:
//Abaixo de R$ 5.000: Desempenho Fraco
//Entre R$ 5.000 e R$ 10.000: Desempenho Regular
//Acima de R$ 10.000: Desempenho Excelente

programa {
  funcao inicio() {
    
    real valorVenda

    escreva("Digite o total de vendas do mês: ")
    leia(valorVenda)

    se (valorVenda < 5000){
      escreva("O desempenho está fraco.")
    } senao{
      se (valorVenda > 10000){
        escreva("O desempenho está excelente.")
      } senao{
        escreva("O desempenho está regular.")
      }
    }
  }
}
