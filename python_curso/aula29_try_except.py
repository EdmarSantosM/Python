"""
    Introdução ao tratamento de erros Exceções
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar

"""

# Exemplo de Erro

# print(123)
# print(789)
# int('a')

# 123
# 789
# Traceback (most recent call last):
#   File "d:\vsCode\curso_python\Python\python_curso\aula29_try_except.py", line 12, in <module>
#     int('a')
# ValueError: invalid literal for int() with base 10: 'a'

numero = input('Dobre o valor do número digitado: ')
numero_float = float(numero)
print(f'O Dobro do {numero} é {numero_float * 2:.2f}')

print()
print('-------------------------------------------------')
print()

# INDICADO SEMPRE  TRATAR  TODA DADO PASSADO PELO USUÁRIO.

numero_str = input('Digite um número : ')
print(numero_str.isdigit()) # Retorna verdadeiro caso seja digitado um número e  falso  caso não.

# Observação  o if e else muda o fluxo (checa a condição), somente  não faz  tratamento de erro.

if numero_str.isdigit():
    numero_float2 = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float2 * 2}')
else:
    print('Isso não é um número !!!')

print()
print('-------------------------------------------------')
print()    

# APLICANDO O TRY / EXCEPT

numero_str2 = input('Vou dobrar o número que voc~e digitou: ')

try:
  print()
  print('Ainda é STR: ',numero_str2)
  print()

  numero_float3 = float(numero_str2)
  print()
  print('Agora é um FLOAT: ',numero_float3)
  print()

  print()
  print(f'O dobro de {numero_str2} é {numero_float3 * 2:2f}')
  print()
except:

    print('Isso não é um número')

print()
print('-------------------------------------------------')
print()    
