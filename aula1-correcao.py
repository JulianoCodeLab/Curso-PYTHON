#----------------------Resolucao 1

entrada  = input('Digite um número: ')

try:

#converte a string que o usuario digitou em inteiro
    entrada_int = int(entrada)

#se o resto da divisão por 2 for 0
    par_impar = entrada_int % 2 ==0

#da um atributo inicial ao objeto como impar
    par_impar_texto = 'impar'

#condiciona o objeto, se o atributo for true, ele é par
    if par_impar:
        par_impar_texto = 'Par'

#exibe mensagem sobre o atributo do objeto
    print(f'O número {entrada_int} é {par_impar_texto}')
except:

#exibe mensagem caso o valor digitado não seja um numero inteiro
    print ('Você não digitou um número inteiro!')