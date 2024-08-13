lista=list ([  1992,24,8,True])

#nos devielve la longitud dela lista(cantidad de caracteres)
cadena="hola"
resultados=len(lista)

# agregando una elemento a la lista

lista.append(4)#agregar el 4

#agregando un elemento en una posicion especifica

lista.insert(2,False)#agrege uh false

# agregando elementos a la lista
lista.extend([2011])

#elimnanos un elemento de la lista
print(len(lista))
lista.pop(0)
lista.pop(-1)

print(len(lista))

# elemento un elemento de la lista por su valor
#lista.remove("Maldonado")

lista.sort()
print(lista)
lista.sort(reverse=True)

elemento_encontrado=lista.index(8)
print(lista)
print(elemento_encontrado)
