#Programa que pede par o usuario digitar um numero inteiro, e informa se o numero for impar ou par


# ----------------------------------Resolução 1 
entrada =input('Digite um número: ')


if entrada.isdigit():

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
else:

#exibe mensagem caso o valor digitado não seja um numero inteiro
    print ('Você não digitou um número inteiro!')

#------------------------------------------Melhor resolução






# ---------------------------------------------------------------------------------------------------------------
#faça um programa que pergunte a hora para o usuario, e baseando se nisso, ele exibe uma saudação apropriada
# 0-11"bom dia"  12-17"boa tarde" 18-23"boa noite"




#faça um programa que peça ao usuario o primeiro nome
#se o nome tiver 4 letras ou menos escreva "seu nome é curto", 
#se tiver entre 5 e 6 "seu nome é normal"
#Maior que 6  escreva "seu nome é muito grande"