'''
    las tuplas son listas inmutables, 
    es decir, no se pueden modificar
    y se declaraan con ()
'''
#tupla=(1,2,3,4,5,6,7,8,9,0)

tupla=("uno","dos","tres")
print(tupla)

tuplaVariada=(12,True,23.5, "hola", 12+4j)
print(tuplaVariada)


tuplaConTupla=(1,2,3,4,(7,8,9))     #Se pueden hacer tuplas dentro de tuplas que sirven para agrupar datos
print(tuplaConTupla)
print(tuplaConTupla[3])
print(tuplaConTupla[-2])
print(tuplaConTupla[0:2])


a,b,c=tupla
print(a,b,c)    #Se pueden asignar los valores de una tupla a variables
print(a)        #Se pueden imprimir los valores de una tupla por separado
print(b)
print(c)



