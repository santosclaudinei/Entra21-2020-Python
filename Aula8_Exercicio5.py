# #--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#           com seus respectivos endereços utilizando as funções do ex3 e ex4

from Exercicio1 import lista_cadastro, cadastro_pessoa
from Exercicio2 import lista_endereco, cadastro_endereco
from Exercicio3 import listar_pessoa, listar_pessoas
from Exercicio4 import listar_endereco, listar_enderecos

while True:                

    print('''
    #################################### SISTEMA ENTRA21 ####################################


    1 - Cadastrar de Dados de Uma Pessoa
    2 - Listar Todos os Cadastrados
    3 - Listar Cadastrados Por ID
    4 - Sair do Sistema


    #########################################################################################
    ''')

    opcao = int(input('Por favor escolha uma das opções listadas acima: '))
    
    if 1 <= opcao <= 4:
        if opcao == 1:
            nome = input('Digite seu primeiro nome: ')
            sobrenome = input('Digite seu ultimo nome: ')
            idade = int(input('Digite sua idade: '))
            cadastro_pessoa(nome, sobrenome, idade)
            if(idade >= 18):
                rua = input('Digite o nome da rua: ')
                numero = int(input('Digite o numero da residencia: '))
                complemento = input('Digite o complemento da residencia: ')
                bairro = input('Digite o nome do bairro: ')
                cidade = input('Digite o nome da cidade: ')
                estado = input('Digite o nome do estado: ')
                ID = len(lista_endereco)+1
                cadastro_endereco(ID, rua, numero, complemento, bairro, cidade, estado)
        elif opcao == 2:
            listar_pessoas(lista_cadastro)
            listar_enderecos(lista_endereco)
        elif opcao == 3:
            IDe = int(input('Digite o ID que deseja pesquisar: '))
            listar_pessoa(IDe)
            listar_endereco(IDe)
        elif opcao == 4:
            print('Obrigado.')
            break