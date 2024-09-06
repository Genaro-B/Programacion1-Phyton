#Enunciado:6) Lee un número por teclado que pida el precio de un producto (puede tener 
#decimales) y calcule el precio final con IVA. El IVA sera una constante que sera del 21%. 
 
#Declarar variables a usar:
IVA=21
precio=int(input("Ingrese el precio del producto:"))
#Agregar Iva al precio del producto:
precio+=(IVA*precio)/100
#Imprimir precio final:
print(f"El precio final con Iva es:{precio}")
