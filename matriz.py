from numpy import *

print ("opciones de archivo: 1)archivo nuevo. 2)leer archivo ")
l=input()
if l=="2":
    print("ingrese el nombre del arhivo a leer (con extension): ")
    name=input()
    n2=input()
    #f=open(name,"r")
    #contenido=f.read()
    a=loadtxt(name)
    b=loadtxt(n2)
    #"a=array([[f.read()],[f.read()],[f.read]])
    print ("el archivo leido es:" + name)
    print (a)
    print (b)
    #f.close()
    print("presione enter parar salir")
    input()
elif l=="1":
    print("ingrese el nombre del arhivo a crear (con extension): ")
    name=input()
    print("ingrese caracteres al nuevo archivo")
    ingresar=input()
    f=open(name,"w")
    f.write(ingresar)
    print ("su nuevo archivo es:" + name)
    print ("el archivo contiene: " + ingresar )
    f.close()
    print("presione enter parar salir")
    input()
else:
    print("opcion no valida, presione enter parar salir")
    input()

