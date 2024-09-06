#Enunciado:13) Pide un número por teclado e indica si es un número primo o no. Un número primo 
#es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, ya que 
#25 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz 
#cuadrada del numero e ir comprobando que si es divisible desde ese número hasta 1. 
#NOTA: Si se introduce un número menor o igual que 1, directamente es no primo.  

import math
divisores=2
numero=int(input("Ingrese un valor:"))
#Calculamos la raiz cuadrada para hacer uso del truco que nos permite evaluar la menor cantidad de numeros posibles
raiz_cuadrada=int(math.sqrt(numero))
print(f"El número {numero} ",end="")
if(numero<=1):
    print("no es primo.")
else:
    for i in range(2,raiz_cuadrada+1,1):
        if(numero%i==0):
            divisores+=1
        
    if(divisores==2):
        print("es primo.")
    else:
        print("no es primo")

            
