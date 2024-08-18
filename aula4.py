"""
Operadores de atribuições
= += -= *= /= //= **= %=
"""
objeto = 1

###

#contador = contador + 1
objeto += 3
print(objeto)


#----------------------------------------------------------------#
#funciona tambem com string, ele concatena as novas strings

contadorStr = '1'

contadorStr += '0'
print(contadorStr)


#----------------------------------------------------------------#
#o multiplicador repete o atributo do objeto N vezes se eu multiplicar uma string
contadorMt = '2'

contadorMt *= 10
print(contadorMt)