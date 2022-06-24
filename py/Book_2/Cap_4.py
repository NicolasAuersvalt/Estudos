"""


"""

"""
Comandos:
list(range(1,5))
min()
max()
sum()
print(lista[2:])
print(lista[:2])
"""
numbers = list(range(1,5))
print(numbers)

"""
List Comprehension (Abrangência de Lista)
comprimir tudo em uma linha

1°
print([number ** 2 for number in range(1,11)])

# Exemplo 1: Até um milhão

print([number for number in range(1, 1000001)]) # Pesado

# Exemplo 2: Ímpares até 100

print([number for number in range(1, 100, 2)]) 

# Exemplo 3: Múltiplos de 3 até 300

print([number for number in range(0, 301, 3)])
"""



