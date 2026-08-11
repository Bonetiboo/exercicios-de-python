# Ex.55 - Crie um dicionário livro com paginas_lidas e total_paginas; calcule o percentual lido e classifique com if.

livro = {
    'paginas_lidas': int(input('Digite o número de páginas lidas: ')),
    'paginas_totais': int(input('Digite o número total de páginas: '))
}

porcentagem_de_leitura = livro['paginas_lidas']/livro['paginas_totais'] * 100

print(f"A porcentagem de leitura é de {porcentagem_de_leitura}%")