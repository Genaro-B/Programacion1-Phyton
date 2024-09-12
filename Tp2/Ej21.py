#Clase Recursividad:
class Recursividad:
   @staticmethod
   def sumar_numeros_hasta_1(numero):
        #Caso  base:
       if(numero>1):
            #Salida recursiva:
            return numero+Recursividad.sumar_numeros_hasta_1(numero-1)
       else:
            #Salida no recursiva:
           return 1




control=True#Creamos una variable que según su valor determinamos si se va a seguir o no iterando sobre el bucle
numero=0#Creamos la variable en donde vamos a guardar el valor que se ingrese por teclado
while(control):
    numero=int(input("Ingrese un numero mayor a 0:"))
    if(numero>0):
        control=False

print(f"El resultado de la suma de los números naturales hasta 1 es:{Recursividad.sumar_numeros_hasta_1(numero)}")