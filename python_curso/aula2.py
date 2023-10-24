# Funcao print
# Exibe a saida na tela / output
# Pode receber argumentos
# Exemplo print(12) ou print(12,34)

print(12)
print(15,35)
print(34,78)

# alterando o formato / estilo do separador
print(100,150, sep=" * ")
print(250,300, sep=' - ')

# sobre as quebras de linhas
# \r\n -> CRLF (windows)
# \n -> LF (Unix)
print(30,40,sep=" ",end='\n##') # Faz a quebra de linha com \n e adiciona o caracter na sequencia
print(500,700, sep='$',end='@@\n')
print(50,60,sep='-',end='\n')
