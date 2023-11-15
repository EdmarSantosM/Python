"""

Fatiamento de strings
012345678

Olá Mundo

-987654321

Fatiamento [i:f:p] [::]

    # i - inicio
    # f - fim
    # p - passo

Obs.: A função len retorna a quantidade de caracteres de string


"""

# FATIAMENTO 

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])

print(variavel[4:]) # Inicia da posição 4 e vai ate o final

print()

# O caractere da posição 5 'ùltimo é omitido'
# Inicia da posição 0 até 4

print(variavel[0:5])
print(variavel[:5])

print()

print(variavel[-8:-2])

print()

# FUNÇÃO len (contagem de caracteres)

variavel_2 = 'Bom dia' 
print(len(variavel_2)) # 7 caracteres contando com o espaço

print()

variavel_3 = 'Boa tarde !!!'

print(variavel_3[0:len(variavel_3):2])

print()

print(variavel_3[::-1]) # -1 exibe de traz para  frente 

print()

