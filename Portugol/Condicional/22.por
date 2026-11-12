//22.	 Você deve criar um programa que classifique o nível de acesso de um usuário com base na sua função. O usuário deve inserir o nome de sua função, e o programa deve indicar qual é o seu nível de acesso.
//As funções e seus níveis de acesso são:
//●	Admin: Nível de acesso 3 (Acesso completo).
//●	Gerente: Nível de acesso 2 (Acesso limitado, mas pode gerenciar usuários).
//●	Funcionário: Nível de acesso 1 (Acesso restrito, apenas pode consultar informações).


programa {
  funcao inicio() {
    
    real cargo

    escreva("Digite sua função:\n1-Admin\n2-Gerente\n3-Funcionário\n")
    leia(cargo)

    se (cargo == 1){
      escreva("Seu nível de acesso é 3 (Acesso completo).")
    } senao{
      se (cargo == 2){
        escreva("Seu nível de acesso é 2 (Acesso limitado, mas pode gerenciar usuários).")
      } senao{
        escreva("eu nível de acesso é 1 (Acesso restrito, apenas pode consultar informações).")
      }
    }
  }
}
