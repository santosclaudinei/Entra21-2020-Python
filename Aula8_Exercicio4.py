#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve exibir todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#    a função deve exibir um endereço cadastrado na função do ex2 filtrando por 
#    id da pessoa

from Exercicio2 import lista_endereco

def listar_enderecos(lista_endereco):
    arquivo = open('dados cadastrados.txt','r')
    for usuario in arquivo:
        dados = usuario.strip().split(';')
        print(f'ID: {dados[3]}\nRua: {dados[4]}\nNumero: {dados[5]}', end='')
        print(f'\nComplemento: {dados[6]}\nBairro: {dados[7]}', end='')
        print(f'\nCidade: {dados[8]}\nEstado: {dados[9]}')
    print('Esses foram os dados de endereços presente no banco de dados.\n')
    arquivo.close()

def listar_endereco(IDe):
    arquivo = open('dados cadastrados.txt', 'r')
    for usuario in arquivo:
        dados = usuario.strip().split(';')
        if dados[3].strip() == str(IDe):
            print(f'ID: {dados[3]}')
            print(f'Rua: {dados[4]}')
            print(f'Numero: {dados[5]}')
            print(f'Complemento: {dados[6]}')
            print(f'Bairro: {dados[7]}')
            print(f'Cidade: {dados[8]}')
            print(f'Estado: {dados[9]}')
        else:
            print('Não existe dados vinculados para esse ID no banco de dados.\n')
    arquivo.close()