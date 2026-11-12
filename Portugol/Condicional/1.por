//As vendas parceladas se tornaram uma ótima opção para os lojistas, que a cada dia criam novas promoções para tentar conquistar novos clientes. 
//Faça um programa onde o lojista possa entrar com o preço do produto e receba as seguintes informações:
//-O valor com 10% de desconto para pagamento à vista
//-O valor da prestação para parcelamento sem juros, em 5x
//- O valor da prestação para parcelamento com juros, em 10x, com 20% de acréscimo no valor do produto

programa {
  funcao inicio() {

    real valor, valorDesconto, valorParc, valorJuros

    escreva("Escreva valor do produto: ")
    leia(valor)

    valorDesconto = valor - (valor * 0.1)
    valorParc = valor / 5
    valorJuros = (valor * 1.2) / 10

    escreva("O valor com desconto é: ", valorDesconto , "\nO valor parcelado em 5x sem juros é: 5x " , valorParc , " \nO valor parcelado em 10x com juros é: 10x " , valorJuros)
  }
}
