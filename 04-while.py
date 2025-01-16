#x=10

'''while x < 10: 
    print(x)
    x=x+1
    
    '''#Operacion de Multiplicacio de AxB utilizando sumas
    #a=3
    #b=4
    #salida: 3+3+3+3=12
    
    
"""
    a1=int(input('Dame el primer numero: '))
    b1=int(input('Dame el segundo numero: '))
    res=a1*b1
    print("el resultado es:", res)
"""
    
a2 = int(input('Dame el primer número: '))
b2 = int(input('Dame el segundo número: '))
i = 1
res = 0
op = ""

while i <= b2:
    res += a2
    op += f"{a2}+"
    i += 1
    
print(f"{op}={res}")





    
