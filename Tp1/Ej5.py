#Enunciado:5) Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es, 
#también debemos indicarlo. 

#Declarar y guardar un valor:
numero=int(input("Ingrese un valor:"))
#Evaluar si el valor es divisible entre 2:
print("Es divisible entre 2? Respuesta:",end="")
if(numero%2==0):
    print("si")#Si el resto de la división es 0  significa que es divisible por ende escribimos si 
else:
    print("no")#En caso de que el resto sea distinto de 0 ,no es divisible y mostramos un no
