
# and - Todas as condicoes precisam ser verdadeiras

# Se qualquer valor for considerado falso a expressao inteira será avaliada naquele valor 

# Sao consideradas "falsy" (0 , 0.0, '', False)

# O tipo None que e usado para representar um 'nao valor'

senha_cadastrada = '123456'

entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha :')

# if(entrada == 'E' and senha_digitada == senha_cadastrada):
#     print()
#     print('Entrar no console')
#     print()
# else:
#     print()
#     print('Sair do console')
#     print()


# # Avaliacao curto circuito
# hifen = ' - ' * 10
# print() 
# print(hifen)
# print( '\t',True and False and True)
# print('\t',True and 0 and True)
# print(hifen)   
# print()

# Utilizando o operador 'or'
if( entrada == 'E' or entrada == 'e') and (senha_digitada == senha_cadastrada):
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
# print( '\t',True and True and True)
# print('\t',True and 0 and True)
print('\t',0 or False or 0 or 'abc') # abc foi  considerada como true (verdadeiro).
print(hifen)   
print()


# Utilizando o operador 'not'
# Usado para inverter valores (expressoes)

# not False = True
# Not True =  False

# Exemplo 01

senha_01 = input('Senha : ')

if senha_01 != '123456':
 #   print('Senha correta')
# else:
   print('Senha incorreta')  