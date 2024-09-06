#Enunciado:9) Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el 
#bucle que desees. 
print("--Numeros del 1 al 100 divisibles entre 2 y 3:")
for i in range(1,101,1):
    if((i%2==0)and(i%3==0)):
        print(f"Nro:{i}")