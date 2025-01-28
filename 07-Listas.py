'''
    Una lista es una secuencia de elementos, la cual se crea con [*]
'''

l1=["Dario",33,1.75,True, "German", 20.0] #Se puede crear una lista con diferentes tipos de datos
print(l1)       #Se puede imprimir la lista completa
print(l1[:])    #Se puede imprimir toda la lista
print(l1[2])    #Se puede acceder a un elemento de la lista por medio de su indice
print(l1[-1])   #Se puede acceder a un elemento de la lista por medio de su indice de manera inversa
print(l1[0:3])  #Se puede imprimir la lista a partir de un indice
print(l1[3:])   #Se puede imprimir la lista a partir de un indice

l1.append("hola")   #Append sirve para agregar un elemento a la lista
print(l1)

l1.insert(2,"Marco") #Insert sirve para agregar un elemento en un indice especifico
print(l1)

l1.extend(["Hola",  #Extend sirve para agregar varios elementos a la lista
           "Mundo", 
           "Cruel"]) 
print(l1)

l1.remove(33)       #Remove sirve para eliminar un elemento de la lista
print(l1)

l1.pop()            #Pop sirve para eliminar el ultimo elemento de la lista
print(l1)


l1.pop(2)           #Pop tambien sirve para eliminar un elemento de la lista por medio de su indice
print(l1)


l2=["tres", "cuatro"]
l3=l1+l2           
print(l3)

print(l2*4)         #Multiplicar una lista por un numero la repite ese numero de veces


l4=[2,1,5,4,3]
print(l4)
print(sorted(l4))   #Sorted sirve para ordenar una lista
print(l4.sort())    

# Estas ultimas 2 funciones son muy parecidas pero la diferencia es que sorted no modifica la lista original

del l4[0]           #Del sirve para eliminar un elemento de la lista por medio de su indice
print(l4)




