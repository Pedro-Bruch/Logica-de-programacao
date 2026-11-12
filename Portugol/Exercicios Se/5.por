//Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o código e o preço de custo de cada 
//produto e calcule o preço novo. Calcule também, a média dos preços com e sem aumento. Mostre o código e o 
//preço novo de cada produto e, no final, as médias.
programa {
  funcao inicio() {
    real preco, precoNovo, media
    inteiro codigo

    escreva("Digite codigo do produto: ")
    leia(codigo)
    escreva("digite valor do produto: ")
    leia(preco)

    precoNovo = preco * 1.2

    media = (precoNovo + preco) / 2

    escreva("Código do produto é: " , codigo, " e o preço novo dele é: " , precoNovo ,  ".\nA média dos preços é: " , media , ". ")
  }
}
