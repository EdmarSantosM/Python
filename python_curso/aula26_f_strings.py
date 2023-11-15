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
print()

print(f'{1000.4873648123746}')
print(f'{100.4873648123746:,.1f}')
print(f'{100.4873648123746:,.13}')
print(f'{100.4873648123746:+,.1f}')
print(f'{100.4873648123746:0=+12,.1f}') # Força o número aparecer antes do zero

print()

print(f'O Hexadecimal de 1500 é {1500:08x}')