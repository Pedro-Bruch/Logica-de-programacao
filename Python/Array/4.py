#4- Faça um programa em Py que alimente um vetor, com um número de posições definidas pelo usuário. 
#Este vetor deverá armazenar um conjunto de nomes em diferentes posições. 
#Crie um mecanismo para alimentar elementos no vetor e pesquisar por um valor existente.
# ======== MENU ======== 
#1) Cadastrar nome 
#2) Pesquisar nome 
#3) Listar todos os nome 
#0) Sair do programa 
#——————– 
#Digite sua escolha:

nomes = []
usuario = 1
posicoes = int(input("digite o número limite de posições: "))

while usuario != 0:
    print("# ======== MENU ========\n1) Cadastrar nome\n2) Pesquisar nome\n3) Listar todos os nomes\n0) Sair do programa\n---------------------")
    usuario = int(input("Digite sua escolha: "))
    
    if usuario == 1:
        quantidade = len(nomes)
        if quantidade >= posicoes:
            print("O número de posições ja chegou no limite.")
        else:
            nome = input("Digite o nome: ").lower()
            nomes.append(nome)
        
    if usuario == 2:
        pesquisa = input("Digite o nome que deseja pesquisar: ").lower()
        if pesquisa in nomes:
            posicao = nomes.index(pesquisa)
            print(f"O nome {pesquisa} está na lista na posição {posicao}")
        else:
            print("Esse nome não está na lista.")
    
    if usuario == 3:
        print(nomes)        