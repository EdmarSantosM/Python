
# Convertendo tipos de dados.

# Exemplo de concatenação
print('a' + 'b')

# É apresentado a senguinte mensagem :

#  File "d:\vsCode\curso_python\Python\python_curso\aula6.py", line 5, in <module>
#     print('1' + 1)
#           ~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# Tipos imutáveis e primitivos:
# str, int, float, bool

# Convertendo a str '1' para int e validando seu tipo
print(int('1'),type(int('1')))

# Convertendo a str '1' para float
print(float('1') + 1)
print(float('1.2') + 1)

print(type(bool('')))
print(bool(''))

print(type(bool(' ')))
print(bool(' '))