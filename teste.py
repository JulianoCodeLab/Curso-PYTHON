Nome = input('Digite seu nome: ')
tamanho_nome = len(Nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('seu nome é muito grande')
else:
    print('Por favor, digite mais de uma letra!')