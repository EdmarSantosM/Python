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

if( nome != "") and (idade != ""):
    print()
    print(f'Seu nome é {nome}')
    print()
    print(f'Nome invertido :', nome[::-1].upper())
    print()

    # validacao de  espaços
    if ' ' in {nome}:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome NÂO contem espaços')
    print()

    print(f'Seu nome tem :', {len(nome)} , 'letras')
    print()
    print(f'A primeira letra do seu nome :',(nome[:1]))
    print()
    print(f'A última letra do seu nome :' ,(nome[4:5]))
    print()
elif ( nome == "") or (idade != ""):
    print()
    print(f'Desculpe você deixou ou o campo "nome" ou "idade" vazios')
    print()

print()
print(hifen)
print()

# OUTRA SOLUCAO SUGERIDA

nome_2 = input('Digite o seu nome: ')
idade_2 = input('Digite sua idade: ')

print(hifen)
print()

if nome_2 and idade_2:
   print(f'Seu nome é {nome_2}')
   print(f'Seu nome invertido é  {nome_2[::-1]}')

   if ' ' in nome_2:
       print(f'Seu nome têm espaços')
   else:
       print(f'Seu nome não têm espaços')

   print(f'Seu nome tem {len(nome_2)} letras')

   print(f'A primeira letra do seu nome {nome_2[0]}')

   print(f'A última letra do seu {nome_2[-1]}')

else:
    print("Desculpe, você deixou campos vazios")

