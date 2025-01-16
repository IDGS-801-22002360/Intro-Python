import os

def funcion1():
    os.system('cls')
    n1 = int(input('Dame el primer numero: '))
    n2 = int(input('Dame el segundo numero: '))
    res = n1 + n2
    print("Resultado: ", res)

def funcion2():
    os.system('cls')
    n1 = int(input('Dame el primer numero: '))
    n2 = int(input('Dame el segundo numero: '))
    res = n1 - n2
    print("Resultado: ", res)

def funcion3():
    os.system('cls')
    n1 = int(input('Dame el primer numero: '))
    n2 = int(input('Dame el segundo numero: '))
    res = n1 * n2
    print("Resultado: ", res)

def funcion4():
    os.system('cls')
    n1 = int(input('Dame el primer numero: '))
    n2 = int(input('Dame el segundo numero: '))
    res = n1 / n2
    print("Resultado: ", res)

def run():
    while True:
        os.system('cls')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Multiplicacion')
        print('4.- Division')
        print('5.- Salir')
        op = int(input('Elige una opcion: '))
        
        if op == 1:
            funcion1() 
        if op == 2:
            funcion2()    
        if op == 3:
            funcion3()
        if op == 4:
            funcion4()
        if op == 5:
            break
        

if __name__ == "__main__":
    run()


