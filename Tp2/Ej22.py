#Clase Recursividad:
class Recursividad:
    @staticmethod
    def sumar_digitos(numero):
        #caso base:
        if(numero==0):
            #salida no recursiva:
            return numero
        else:
            #salida recursiva:
            return (numero%10)+Recursividad.sumar_digitos(numero//10)
#Se crea una variable llamada número y se lee un valor por teclado:   
numero=int(input("Ingrese un numero para sumar sus digitos:"))
#hacemos uso del metodo recursivo mediante la clase a la que esta asosiado:
print(f"La suma de los digitos es igual a {Recursividad.sumar_digitos(numero)}")