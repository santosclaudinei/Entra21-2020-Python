#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#        a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

from Exercicio1 import lista_cadastro

def listar_pessoas(lista_cadastro):
    arquivo = open('dados cadastrados.txt','r')
    for usuario in arquivo:
        dados = usuario.strip().split(';')
        print(f'Nome: {dados[0]}\nSobrenome: {dados[1]}\nIdade: {dados[2]}')
    print('Esses foram os dados de pessoas presentes no banco de dados.\n')
    arquivo.close()

        
def listar_pessoa(ID):
    arquivo = open('dados cadastrados.txt', 'r')
    for usuario in arquivo:
        dados = usuario.strip().split(';')
        if dados[3].strip() == str(ID):
            print(f'Nome: {dados[0]}')
            print(f'Sobrenome: {dados[1]}')
            print(f'Idade: {dados[2]}')
        else:
            print('Não existe dados vinculados para esse ID no banco de dados.\n')
    arquivo.close()