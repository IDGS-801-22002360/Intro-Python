t1 = "Hola"
t2 = "mundo"

Tfinal = t1+" "+t2
print(Tfinal)

print("el saludo es: %s %s" %(t1,t2))

saludo="saludo: {x}{y}".format(x=t1,y=t2)
print(saludo)

texto="Desarrollo Web Profesional"
print(texto)
print(texto.lower())  #lowercase
print(texto.upper())  #uppercase
print(texto.title())
print(texto.find("Web"))
print(texto.count("e"))

print(texto.replace('e','a'))

cadenaSplit=texto.split(" ")
print(cadenaSplit)
