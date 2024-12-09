""" Calculadora com while"""

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')

    operador = input('Digite o operador(+-/*): ')

    num_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        num_validos = True
    except:
        num_validos = None


    """PONTO DE VALIDAÇÃO DA CALCULADORA! """
    if num_validos is None:
        print('Um ou ambos numeros digitados são invalidos! ')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido. ')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador! ')
        continue




    ###
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    else:
        print('Nunca deve chegar aqui, mas chegou! ')

    sair = input('Quer sair [s]im: ').lower().startswith('s')


    if sair:
        break

