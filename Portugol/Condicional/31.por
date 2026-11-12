//Peça ao usuário para inserir o valor de um salário bruto e, calcule o imposto a ser pago com base na faixa de rendimento. O programa deve considerar as seguintes faixas de imposto:
//●	De 0 a 1.000: Isento de imposto.
//●	De 1.001 a 3.000: Imposto de 10%.
//●	De 3.001 a 5.000: Imposto de 15%.
//●	Acima de 5.000: Imposto de 20%.
//O programa deve exibir o valor do imposto e o salário líquido (salário bruto menos o imposto).

programa {
  funcao inicio() {
    
    real salario, conta, conta1

    escreva("Digite seu salário: ")
    leia(salario)

    se (salario >= 0 e salario <= 1000){
      escreva("Isento de imposto")
    } senao{
      se (salario > 1000 e salario <= 3000){
        conta = salario * 0.1
        conta1 = salario - conta
        escreva("Deverá ser pago 10% de imposto, que é: ", conta ,"\nO salário final ficará: ", conta1)
      } senao{
        se (salario > 3000 e salario <= 5000){
          conta = salario * 0.15
          conta1 = salario - conta
          escreva("Deverá ser pago 15% de imposto, que é: ", conta ,"\nO salário final ficará: ", conta1)
        } senao{
          conta = salario * 0.2
          escreva("Deverá ser pago 20% de imposto, que é: ", conta)
        }
      }
    }
  }
}
