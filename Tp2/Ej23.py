#Clase Recursividad:
class Recursividad:
    @staticmethod
    def mostrar_cadena_inversa(cadena,indice):
        #Caso base:
        if indice==0:
            #Salida no recursiva:
            print(cadena[indice])
        else:
            #Salida recursiva:
            print(cadena[indice],end="")
            Recursividad.mostrar_cadena_inversa(cadena,indice-1)

cadena=input("Ingrese una palabra o frase:")
print("------CADENA INVERSA------")
Recursividad.mostrar_cadena_inversa(cadena,len(cadena)-1)