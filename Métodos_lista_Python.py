# append()
# Append significa incluir ou anexar. Este método adiciona um elemento no final da lista.
food = ["pasta", "pizza", "lasagna"]
food.append("spaghetti")
print(f'Metodo append() {food}')
# Resultado:
#     ['pasta', 'pizza', 'lasagna', 'spaghetti']




# clear()
# Clear significa limpar. Este método apaga todos os elementos de uma lista.
food = ["pasta", "pizza", "lasagna"]
food.clear()
print(f'Metodo clear() {food}')




# copy()
# Copy significa copiar. Este método retorna uma cópia da lista.
food = ["pasta", "pizza", "lasagna"]
food.copy()
print(f'Metodo copy() {food.copy()}')





# count()
# Count significa contar. Este método retorna o número de elementos que contenham o valor especificado.
food = ["pasta", "pizza", "lasagna"]
x = food.count("pizza")
print(f'Metodo count() Usa {food.count("pizza")} ou {x}')
# Resultado:
#     1






# extend()
# Extend significa estender. Este método adiciona os elementos de uma lista ao final de outra lista.
food = ["pasta", "pizza", "lasagna"]
dessert = ["chocolate", "gelato"]
food.extend(dessert)
print(f'Metodo extend() {food}')
# Resultado:
#    ['pasta', 'pizza', 'lasagna', 'chocolate', 'gelato']






# index()
# Index significa índice. Este método retorna a posição do primeiro elemento que contenha o valor especificado.
food = ["pasta", "pizza", "lasagna"]
x = food.index("pizza")
print(f'Metodo inex() Usa {food.index("pizza")} ou {x}')
# Resultado:
#     1






# insert()
# Insert significa inserir. Este método adiciona um elemento a uma posição específica.
food = ["pasta", "pizza", "lasagna"]
food.insert(1, "spaghetti")
print(f'Metodo insert() {food}')
# Resultado:
#     ['pasta', 'spaghetti', 'pizza', 'lasagna']







# pop()
# Pop significa estourar. Este método remove um elemento de uma posição específica.

food = ["pasta", "pizza", "lasagna"]
food.pop(1)
print(f'Metodo pop() {food}')
# Resultado:
#     ['pasta', 'lasagna']







# remove()
# Remove significa remover. Este método remove o primeiro item com o valor especificado.
food = ["pasta", "pizza", "lasagna"]
food.remove("lasagna")
print(f'Metodo remove() {food}')
# Resultado:
#     ['pasta', 'pizza']






# reverse()
# Reverse significa reverter. Este método reverte a ordem da lista.
food = ["pasta", "pizza", "lasagna"]
food.reverse()
print(f'Metodo reverse() {food}')
# Resultado:
#     ['lasagna', 'pizza', 'pasta']




# sort()
# Sort significa ordenar. Este método ordena a lista alfabeticamente.
food = ["pasta", "pizza", "lasagna"]
food.sort()
print(f'Metodo sort() {food} ')
# Resultado:
#     ['lasagna', 'pasta', 'pizza']