#Enunciado:4) Declara 2 variables numéricas (con el valor que desees), he indica cual es mayor de 
#los dos. Si son iguales indicarlo también. Ves cambiando los valores para comprobar 
#que funciona. 

#Declarar variables:
numero1=75;
numero2=4;
#Evaluar condición y imprimir mensaje según corresponda:
print("Resultado:",end="")
if(numero1>numero2):
    print(f"{numero1} es el mayor.")
elif(numero2>numero1):
    print(f"{numero2} es el mayor.")
else:
    print(f"{numero1} y {numero2} son iguales.")
