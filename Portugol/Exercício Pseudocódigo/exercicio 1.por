//Leia três notas e calcule a média.
programa {
  funcao inicio() {
    real nota1, nota2, nota3, media
    escreva("Escreva a primeira nota: ")
    leia(nota1)
    escreva("Escreva a segunda nota: ")
    leia(nota2)
    escreva("Escreva a terceira nota: ")
    leia(nota3)
    media = (nota1 + nota2 + nota3) / 3
    escreva("A media das notas é: " , media)
  }
}
