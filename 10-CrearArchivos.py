"""

"""

from io import open
import math     # Libreria para funciones matematicas

l=""
t1=open("archivo.txt","r")  #se crear un archivo, y despues se define para que se quiere, como leer, escribir, binario, etc
l=t1.read()                 #se lee el archivo
print(l)

l=t1.readlines()
print(type(l))              #se imprime el tipo de dato de la variable

for i in l:
    print(i)

t1.close()


"""
    pasos de funcionamiento:
    - primero debe mostrar un menu que muestre si se quiere comprar o terminar para hacer corte
    - luego debe pedir el nombre de la persona
    - luego cuantas persona van con el que va a comprar
    - despues cuantos boletos van a comprar

    - despues va a verificar que no exceda el numero de boletos por persona, Maximo 7 boletos
        por persona
    - por ultimo, despues de verificar debe dar la oportunidad cambiar la cantidad de personas 
        o de boletos
    
    - ademas, si la persona compra mas de 5 boletos recibira un descuento de %15 sobre el valor 
        a pagar
    - y si en caso de pagar con la terjeta  CINECO tendra un %10 de descuento adicional al %15 ya
        aplicado en caso de haber comprado 5 boletos, si no compra mas de 5, solo se aplicara el 
        %10 de decuento
    
    - al final debe de escribir en un archivo de texto el nombre de la persona y el total a pagar
    
    - al final cuando se cierre el programa, se debera hacer un corte total de todas las compras
        en la consola, no en el archivo de texto
    
"""