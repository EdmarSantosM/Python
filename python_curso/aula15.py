# Exemplo

nome = input('Qual seu nome? ')
print()

print(nome)

print()
print(f'O seu nome é {nome}')

print()

nome2 = input('Digite seu nome: ')

print()

print(f'Olá!{nome2=}')

print()

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos numeros {numero_1 + numero_2}') # Neste  caso sera  concatenado os valores

# Pode fazer, porém não é boa prática (Type Casting)

# Pois  quebra o programa logo de inicio, não permitindo o desenvolvedor fazer a chegagem

    # Traceback (most recent call last):
    #   File "d:\vsCode\curso_python\Python\python_curso\aula15.py", line 27, in <module>
    #     numero_1 = int(input('Digite um número: '))
    #                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # ValueError: invalid literal for int() with base 10: 'a'

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número'))

print()

print(f'A soma de {numero_1 + numero_2}')



