import os

campos = ('Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa')

usuarios = []


while True:
    print('1 - Cadastrar usuário.')
    print('2 - Listar usuários.')
    print('3 - Alterar usuário.')
    print('4 - Cadastrar usuário.')
    print('5 - Cadastrar usuário.')
    print('6 - Cadastrar usuário.')
    
    
    novo_cadastro = input('Inserir novo cadastro de pessoa na lista: ')

    if novo_cadastro != '':
        cadastros.append(chaves)
        continue
    else:
        break


for chave in pessoa:
    print(f'{chave} {pessoa.get(chave)} ')
