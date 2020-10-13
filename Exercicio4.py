#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve exibir todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#    a função deve exibir um endereço cadastrado na função do ex2 filtrando por 
#    id da pessoa

from Exercicio2 import lista_endereco

def listar_enderecos(lista_endereco):
     for endereco in lista_endereco:
        for ch, val in endereco.items():
            print(ch, ' : ', val)
     print('Esses foram os dados presente no banco de dados.\n')
    

def listar_endereco(IDe):
    for endereco in lista_endereco:
        for val in endereco.values():
            if val == IDe:
                    print('Rua', ' : ', endereco['Rua'])
                    print('Numero', ' : ', endereco['Numero'])
                    print('Complemento', ' : ', endereco['Complemento'])
                    print('Bairro', ' : ', endereco['Bairro'])
                    print('Cidade', ' : ', endereco['Cidade'])
                    print('Estado', ' : ', endereco['Estado'])
    print('Esses foram os dados vinculados a esse ID no banco de dados.\n')
