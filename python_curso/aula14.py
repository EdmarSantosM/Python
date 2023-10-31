# Método format

# variáveis
a = 'AaaA'
b = 'BbbB'
c = 1.1

string = 'a={} b={} c={:.2f}'

formato = string.format(a , b , c)  
# ver sobre  argumentos
# Exemplo ( x, p, t, o)

# ver sobre parametros nomeados 
# Exemplo : (nome1=a, nome2=b, nome3=c)

string = 'b={nome1} a={nome2} c={nome3:.2f}'
formato2 = string.format(nome1=a, nome2=b, nome3=c)


print(formato)
print()
print(formato2)
