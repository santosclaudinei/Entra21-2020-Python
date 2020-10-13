# #--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, 
#          bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

lista_endereco = []

def cadastro_endereco(id, rua, numero, complemento, bairro, cidade, estado):
    while True:
        if rua == '' or complemento == '' or bairro == '' or cidade == '' or estado == '' and numero < '0':
            return print('Um ou mais campos podem ter sidos deixados em branco ou digitados errados.')
        else:
                
            endereco = {}
            endereco['ID'] = id   
            endereco['Rua'] = rua   
            endereco['Numero'] = numero
            endereco['Complemento'] = complemento
            endereco['Bairro'] = bairro
            endereco['Cidade'] = cidade
            endereco['Estado'] = estado
            
            lista_endereco.append(endereco)

            return print('Dados cadastrados com sucesso.')
