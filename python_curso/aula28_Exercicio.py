"""
Exercicio :

    Peça para o usuário digitar seu nome
    Peça para o usuário digitar sua idade

    Se o nome e idade forem digitados:
        Exiba :
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras

            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}

    Se nada for digitado em nome ou idade : Exiba " Desculpe, você deixou campos vazios."        

"""

# Variaveis

hifen = ' - ' * 30

print(hifen)
print()
nome = input('Digite seu nome : ')
idade = int(input('Digite sua idade : '))
print()
print(hifen)

if( nome != "" and idade != ""):
    print()
    print(f'Nome invertido :', nome[::-1].upper())
    print()
    print(f'Seu nome tem :', {len(nome)} , 'letras')
    print()
    print(f'A primeira letra do seu nome :',(nome[:1]))
    print()
    print(f'A última letra do seu nome :' ,(nome[4:5]))
    print()

