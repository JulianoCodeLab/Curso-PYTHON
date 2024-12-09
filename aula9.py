frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'python foi criado por Guido van Rossum.'

i = 0
while i < len(frase):
    letra_atual = frase[i]
    contador_letra = frase.count(letra_atual)

    print(letra_atual, contador_letra)
    i += 1