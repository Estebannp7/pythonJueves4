#variable  de control
contador = 0

#contador de negativos
contadorNegativos = 0

while(contador<5):
    numero=int(input("Digite un numero: "))

    if(numero<0):
        contadorNegativos= contadorNegativos+1
    else:
        contadorNegativos = contadorNegativos


    contador = contador+1    
print(f'el numero de negativos ingreados fue de {contadorNegativos}')  