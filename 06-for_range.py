
range(20)               #Genera una lista hasta un numero antes que le indique ya que cuenta el 0

x = range(10,20)        #Gernera una lista con un rango entre los numeros que le indique

x = range(10,20, 2)     #Gernera una lista con un rango entre los numeros que le indique avanzando de 2 en 2

for i in range(20):     #Imprime los numeros del 0 al 19
    print(i)



n1=int(input('Dame un numero a multiplicar: ')) # Es una operacion que va a imprimir el numero que ingrese por 10
res=0
for j in range(1,11):
    res+=n1
    print(f"{n1}x{j}={res}")


#Los Commits van con la fecha del dia y el tema hasta el que se llego