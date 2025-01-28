"""
    NOTAS:
        - Hacer un metodo para pedir los numeros y no pedirlos en el main
"""


class distancia:
    x1=0
    x2=0
    y1=0
    y2=0
    dis=0
    
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    
    def datos(self):
        self.x1=int(input("Dame el valor de x1: "))
        self.x2=int(input("Dame el valor de x2: "))
        self.y1=int(input("Dame el valor de y1: "))
        self.y2=int(input("Dame el valor de y2: "))
    
    def calcular(self):
        self.dis=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
        print("La distancia entre los puntos es: {}".format(self.dis))

def main():
    x1=int(input("Dame el valor de x1: "))
    x2=int(input("Dame el valor de x2: "))
    y1=int(input("Dame el valor de y1: "))
    y2=int(input("Dame el valor de y2: "))
    obj=distancia(x1,x2,y1,y2)
    obj.calcular()


if __name__ == '__main__':
    main()


