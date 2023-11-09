
"""
Exercicio de fixação

"""

# declaracao de variaveis

primeiro_valor = int(input(' Digite o primeiro valor :'))
segundo_valor  = int(input(' Digite o segundo valor  :'))
hifen = '-' * 150

if(primeiro_valor > segundo_valor):
    print()
    print(hifen)
    print(f'Primeiro valor digitado é"{primeiro_valor}"  maior que o Segundo Valor digitado "{segundo_valor}"')
    print(hifen)
    print()
elif( segundo_valor > primeiro_valor):
    print()
    print(hifen)
    print(f'Segundo valor digitado é "{segundo_valor}"  maior que o Primeiro Valor digitado "{primeiro_valor}"') 
    print(hifen)
    print()   
else :
    (primeiro_valor == segundo_valor) or (segundo_valor == primeiro_valor)
    print()
    print(hifen)
    print(f'Primeiro valor digitado "{primeiro_valor}" e Segundo valor digitado "{segundo_valor}" são iguais')
    print(hifen)
    print()
# elif( primeiro_valor == '') or (segundo_valor == ''):
#     print()
#     print(hifen)
#     print('Valor não identificado')
#     print(hifen)
#     print() 
# else:
#     print()
#     print(hifen)
#     print()
#     print(hifen)
#     print()   



  


