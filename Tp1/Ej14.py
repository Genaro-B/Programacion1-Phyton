#Enunciado:14) Codifique un programa de consola en Java que permita realizar las siguientes 
#acciones:  
#Generar un número aleatorio entre 0 y 100, para ello use la siguiente función: 
#random.randint(0, 100) 
#Una vez generado el número codifique la lógica necesaria para encontrar el número 
#aleatorio ayudando al usuario informando al mismo si el número ingresado es mayor o 
#menor al número aleatorio buscado. Una vez encontrado el número muestre la 
#cantidad de intentos necesarios para lograrlo. 

import random
intentos=0
#Generamos un aleatorio con el uso de la funcion randint de random:
aleatorio=random.randint(0,100)
valor_a_leer=-1
while(valor_a_leer!=aleatorio):
    valor_a_leer=int(input("Ingrese un valor entre el 0 y 100:"))
    intentos+=1
    if(valor_a_leer>aleatorio):
        print("-Es mayor")
    elif(valor_a_leer<aleatorio):
        print("-Es menor")
    else:
        print(f"-Encontró el valor oculto! / Aleatorio:{aleatorio}/ Intentos requeridos:{intentos}")


print("--Fin programa--")
