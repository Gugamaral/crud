import os

chaves = ('Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa')
cadastros = []


while True:
    novo_cadastro = input('Inserir novo cadastro de pessoa na lista: ')

    if novo_cadastro != '':
        cadastros.append(chaves)
        continue
    else:
        break


for chave in pessoa:
    print(f'{chave} {pessoa.get(chave)} ')
