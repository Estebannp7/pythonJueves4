''''
numero=5


while(numero<10):
    print("estoy adentro de la cuerda")
    numero+=1
else:
    print("adios")

print("estoy por fuera de la cuerda")    
'''



opcion=1
print("*****Menu*******")
print("1. SUMAR")
print("2. RESTAR")
print("0. SALIR")


while(opcion != 0):
    opcion=int(input("Digite una opcion: "))
    if(opcion ==1):
        print("sumando")
    elif(opcion==2):
        print("Restando")    
    else:
        print("Digite una opcion valida")
