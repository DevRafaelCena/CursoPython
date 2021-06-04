"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista = ['A', 'B', 'C', 'D', 'E']
print(lista[0:3])
print(lista[:3])
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.insert(2, 9)
print(l1)
print(l2)

l2.append(7)
print(l2)
l1.extend(l2)

print(l1)

print(max(l1))
print(min(l1))

l1.clear()
print(l1)


l3 = list(range(0, 10, 2))
print(l3)

for secreto in l3:
    print(secreto)