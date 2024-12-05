nome = 'Juliano Ambrosio'

indice = 0
novoNome = ''

while indice < len(nome):
    letra = nome[indice]
    novoNome += F'*{letra}'
    indice += 1

    

print(novoNome)