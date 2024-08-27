"""
Interando strings com while
"""

#       0123456789... 
nome = 'Juliano Ambrosio' # interaveis

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print(nome[3])
print(' ')

nova_str = ''

nova_str += 'J*U*L*I*A*N*O A*M*B*R*O*S*I*O'


#------------------------- RESOLUÇÃO

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1
print(novo_nome)