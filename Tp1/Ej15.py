numero=int(input("Ingrese un valor:"))
suma=0
auxiliar=0
logico=False
print("Se cumple los criterios de divisibilidad de los siguentes numeros:")
#Comprobamos si es divisible entre 2 según sus criterios:
#La última cifra debe terminar en 2.
if((numero%10)%2==0):
    print("2")
    logico=True
#Comprobamos si es divisble entre 3 según sus criterios:
#La suma de sus digitos debe ser divisible entre 3.
auxiliar=abs(numero)
while(auxiliar>0):
    suma+=auxiliar%10 #Suma el último digito.
    auxiliar//=10     #Elimina el último digito.

if(suma%3==0):
    print("3")
    logico=logico and True
else:
    logico=False
#Comprobamos si es divible entre 4 según sus criterios:
#El numero que se forma con sus ultimos 2 digitos debe ser divisible por 4
if((numero%100)%4==0):
    print("4")
#Comprobamos si es divisible entre 5 según sus criterios:
#Debe terminar entre 0 y 5.
if((numero%10)==0 or (numero%10)==5):
    print("5")


#Comprobamos si es divisible entre 6 según sus criterios:
#Debe ser divisible por 2 y 3 
if(logico):
    print("6")



