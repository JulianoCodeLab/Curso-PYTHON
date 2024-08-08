#Variaveis imutaveis: str, int, float, bool
#Não pode ser mudada, para mudar uma variavel eu "não mudo!" e sim CRIO UMA NOVA

string = 'juliano'

#Criei uma nova variavel, concatenei o atributo da primeira com modificação
outra_variavel = f'{string[:3]}ABC' 
print(outra_variavel)

#capitalize coloca a primeira letra maiuscula
print(string.capitalize())

#zfill() - completa a largura da string com zeros a esquerda até preencher o tamanho em parametro
print(string.zfill(100))