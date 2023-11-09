
# and - Todas as condicoes precisam ser verdadeiras

# Se qualquer valor for considerado falso a expressao inteira será avaliadanaquele valor como falso

# Sao consideradas "falsy" (0 , 0.0, '', False)

# O tipo None que e usado para representar um 'nao valor'

senha_cadastrada = '123456'

entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha :')

if(entrada == 'E' and senha_digitada == senha_cadastrada):
    print()
    print('Entrar no console')
    print()
else:
    print()
    print('Sair do console')
    print()


# Avaliacao curto circuito
hifen = ' - ' * 10
print() 
print(hifen)
print( '\t',True and False and True)
print('\t',True and 0 and True)
print(hifen)   
print()