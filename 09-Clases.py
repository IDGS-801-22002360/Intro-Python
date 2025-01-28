'''
   Las clases son un tipo de dato que nos permite agrupar 
   datos y funciones en un solo lugar. 
'''

class OperasBas:
    #Declaracion de Propiedades
    n1=0        #Propiedad Publica
    #   _n2=0   #Propiedad Privada
    #   __n3=0  #Propiedad Protegida
    
    n2=0
    res=0
    
    #Declaracion del Constructor this es el equivalente a self en python
    def __init__(self,n1,n2): # si no tiene parametros de todos modos se pone self
        self.n1=n1  #tenemos que poner self para que se pueda acceder a la propiedad
        self.n2=n2
    
    def suma(self):
        self.res=self.n1+self.n2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        self.res=self.n1-self.n2
        print("La resta es: {}".format(self.res))
    
    
    #Declaracion de Metodos o Funciones
    

def main():
    obj=OperasBas(3,4)
    obj.suma()
    obj.resta()

if __name__ == '__main__':
    main()



    