//10.Bolsa de estudos. Leia a média e a renda familiar. O aluno recebe bolsa se: média >= 8 E renda <= 3000.
programa {
  funcao inicio() {
    real media, renda
    escreva("Qual a média da família?")
    leia(media)
    escreva("Qual a renda da família?")
    leia(renda)

    se (media >=8 e renda <= 3000){
      escreva("O aluno recebe bolsa.")
    }senao {
      escreva("O aluno não recebe a bolsa.")
    }
  }
}