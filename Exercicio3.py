#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#        a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

from Exercicio1 import lista_cadastro

def listar_pessoas(lista_cadastro):
    for pessoa in lista_cadastro:
        for ch, val in pessoa.items():
            print(ch, ' : ', val)
    print('Esses foram os dados presente no banco de dados.\n')
            
        
def listar_pessoa(ID):
    for pessoa in lista_cadastro:
        for val in pessoa.items():
            if val == pessoa['ID']:
                print('Nome', ' : ', pessoa['Nome'])
                print('Sobrenome', ' : ', pessoa['Sobrenome'])
                print('Idade', ' : ', pessoa['Idade'])
    print('Esses foram os dados vinculados a esse ID no banco de dados.\n')

