"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
- Chave e valor são separados por dois pontos 'chave:valor';
- Tanto chave quanto valor, pode ser de qualquer tipo de dado;
- Podemos misturar tipos de dados;


# Criação de Dicionários
# Forma 1 (mais comum)

paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
#print(paises['ru'])

# Caso tentamos utilizar uma chave que não existe: KeyError

# Forma 2: Acessando via get (recomendada)
print(paises.get('br'))

# Caso o get não encontre o objeto com a chave informada, será inforemado o valor None
print(paises.get('ru'))

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave não informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}

# Podemos verificar se uma chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Tuplas, por exemplo são bastante interessantes para serem usadas como chave de
dicionário por serem imutáveis

localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))


receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 (mais comum)
receita['abr'] = 350

print(receita)

# Forma 2
novo_dado = {'mai':500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1: a forma de adicionar elementos ou atualizar é a mesma.
# Conclusão 2: em dicionários, não pode haver chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 (mais comum)
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, caso não encontre, KeyError
# OBS 2: Ao remover o objeto, o valor eliminado é exibido

# Forma 2
del receita['fev']
print(receita)

# OBS: Neste caso, o valor eliminado não é exibido


# Imagine que você tem um comércio eletrônico onde temos um carrinho de compras na qual adicionamos produtos

# Poderíamos utilizar uma lista para isso? SIM
carrinho = []
produto1 = ['PlayStation 4', 1, 2300.00]
produto2 = ['God Of Warm', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamod que saber qual é p índice  de cada informação do produto

#2 Poseríamos utilizar uma tupla para isso? SIM


produto1 = ('PlayStation 4', 1, 2300.00)
produto2 = ('God Of Warm', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)


#2 Poseríamos utilizar um dicionário para isso? SIM

carrinho = []
produto1 = {'nome': 'PlayStation 4', 'quantidade':1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade':1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produto do carrinho
# Podemos ter certeza sobne cada informação


# Limpar o dicionário (zerar dados)
d.clear()
print(d)

# Métodos dicionáaro
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# copiando um dicionário para outro
# Forma 1 (deep copy)
novo = d.copy()
print(novo)
novo['d'] = 4

print(d)
print(novo)


# Forma 2
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)



# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele irá gerar para cada valor do iterável uam chave que ira atribuir o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
"""

