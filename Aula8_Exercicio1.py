# #--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

lista_cadastro = []

def cadastro_pessoa(pri_nome, ult_nome, idad):

     if idad >= 18:
                pessoa = {} 
                pessoa['Nome'] = pri_nome
                pessoa['Sobrenome'] = ult_nome
                pessoa['Idade'] = idad
                pessoa['ID'] = len(lista_cadastro)+1
                
                arquivo = open('dados cadastrados.txt','a')
                arquivo.write(f"{pessoa['Nome']};{pessoa['Sobrenome']};{pessoa['Idade']}; ")
                arquivo.close()
                
                lista_cadastro.append(pessoa)
                print('Pessoa cadastrada com sucesso.')
                return pessoa['ID']
                
     else:
            return print('Informações não cadastradas. Menor de idade.')    
        