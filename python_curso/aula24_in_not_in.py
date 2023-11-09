# in e not in

# Strings sao  iteraveis

# 0 1 2 3 4 5

# e d m a r

# nome = 'Edmar'
# print(nome[2])
# print('m' in nome)
# print('z' in nome)
# print(15 * '-')
# print('ma' not in nome)
# print('z' not in nome)

# Exemplo
nome_completo = input(' Digite seu nome completo : ')
encontrar =  input(' Digite a letra que deseja encontrar : ')

if encontrar in nome_completo:
    print(f'{encontrar} esta em {nome_completo}')
else:
    print(f'{encontrar} não está em {nome_completo}')

