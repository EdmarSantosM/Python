"""

Formatação Básica
s - string
d - int
f - float

.<numeros de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)

> - Esquerda
< - Direita
^ - Centro

Sinal - ou +
Exemplo : 0> - 100,.1f

Conversion flags - !r !s !a


"""

#Exemplo com Pading
variavel = 'ABC'
print()
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:$^10}')