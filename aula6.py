"""
Continuação = While + while(laços internos)
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

#Usado para criar tabelas, while dentro do while
while linha <= qtd_linhas:
    coluna = 1

#while interno.
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1


print('Acabou!')
