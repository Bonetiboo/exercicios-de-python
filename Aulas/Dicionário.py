import pandas as pd

# Estrutura com lista

time = ['A', 'B', 'C']
vitória = [10, 9, 6]
estado = ['SP', 'SP', 'RJ']

# Estrutura com dicionário

dic = {
    'time': ['A', 'B', 'C'],
    'vitória': [10, 9, 6],
    'estado': ['SP', 'SP', 'RJ'] 
}

print(dic)

dataframe = pd.DataFrame(dic)

# Estrutura com get

produto = dict(nome='notebook', preço=3500)

print(produto.get('marca', 'não informado')) # ele apenas busca uma informação
# no dicionário específico

# Estrutura com input()

cliente = {}

cliente['nome'] = input("Digite seu nome: ")
cliente['idade'] = input("Digite sua idade: ")

print(cliente)

# Estrutura com pop()

cliente2 = {
    'nome': "Ana",
    'idade': 30   
}
cliente2['idade'] = 31
cliente2.update({'tel': '11999999999'})
del cliente2['nome']
cliente2.pop('tel')
print(cliente2)

# Estrutura com condição

produto = {'preco': int(input("Qual o valor: ")), 'estoque': 3}

if produto['preco'] >= 1000:
    categoria = 'Alto valor'
elif produto['preco'] >= 200:
    categoria = 'Médio valor'
else:
    categoria = "Baixo valor"
    
print(categoria)
print(produto)

# Estrutua com keys, values e items

cliente3 = {
    'nome': "Ana",
    'idade': 31,
    'cidade': "SP"
}

print(cliente3.keys())
print(cliente3.values())
print(cliente3.items())

# Iteração

estoque = {
    'maçã': 10,
    'banana': 5,
    'laranja': 8
}

for fruta in estoque:
    print(fruta)