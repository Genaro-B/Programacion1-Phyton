#Enunciado:10) Lee un número por teclado y comprueba que este número es mayor o igual que 
#cero, si no lo es lo volverá a pedir (do while), después muestra ese número por 
#consola. 

#Bucle while (Simulación del do while):
valor=0
while(True):
    valor=int(input("Ingrese un número:"))
    if(valor>=0):
        break

print(f"El número es:{valor}")