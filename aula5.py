"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> Quando um codigo não tem fim

"""

#ex:
contador = 0

while contador <= 100:
    contador += 1


#expressão condicional que pula a condicional
    if contador == 6:
        print('pula o numero 6')
        continue

#é possivel colocar quantas vezes quiser, de qualquer maneira, ex:
    if contador >= 10 and contador <= 20:
        print('não vou mostrar o ',contador)
        continue


    print(contador)

#toda vez que coloca um 'break' ela encerra o codigo
    if contador == 40:
        break


print('Acabou!')

#sem o if ele contaraa até 11