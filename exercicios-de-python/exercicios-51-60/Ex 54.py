# Ex.54 - Crie um dicionário conta com titular e saldo. Peça um valor de saque; se maior que o saldo imprima 'Saldo insuficiente'.

conta = {
    'titular': 'Rafael',
    'saldo': 10000
}

saque = int(input('Digite o valor o qual deseja sacar: '))

if saque > conta['saldo']:
    print('Saldo insuficiente.')
else:
    print('Sacado com sucesso!')