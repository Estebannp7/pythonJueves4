#variable de control

numero = 5
#acumulador
suma = 0
#declaro el ciclo
while(numero>0):

#pedir un numero
    numero=int(input("digite un numero: "))

    if(numero>=0):
        suma= suma+numero 
    else:
        print(f'la suma fue:  {suma} ')
        break
else:
    print(f'la suma fue:  {suma} ')