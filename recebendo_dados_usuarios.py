"""
Recebendo dados de usuários

input -> todos dados recebidos por inpur será String
"""
# print("Qual seu nome?")
# nome = input()  # Input -> Entrada
nome = input('Qual seu nome?')

# print('Qual sua idade?')
# idade = input()
idade = int(input('Qual sua idade?'))

# Processamento

# Saída
# Print formato python 2.x
# print('%s tem %s anos!' % (nome, idade))

# Print formato python 3.x
# print('{0} tem {1} anos!'.format(nome, idade))

# Print forma mais atual 3.7
print(f'{nome} tem {idade} anos!')
print(f'{nome} nasceu em {2022 - int(idade)}')



