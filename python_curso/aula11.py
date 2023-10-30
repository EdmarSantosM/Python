
# 1. (n + n)
# 2. **
# 3. * , / , // , %
# 4. + , 1

#  1 ** 5
#  1 + 1 + 5
conta_1 = 1 + 1 ** 5 + 5  
print(conta_1)

print()

conta_com_precedencia = (1 + 1) ** (5 + 5) # resultado 1024
print(conta_com_precedencia)

print()

#conta_2 = (1 + int(0.5 + 0.5)) ** 5 + 5 # resultado 37

#conta_2 = 1 + int(0.5 + 0.5) # resultado 2

conta_2 = (1 + int(0.5+0.5)) ** (5 + 5) # resultado 1024

print(conta_2)