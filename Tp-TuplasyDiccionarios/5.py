numeros = (1, 2, 2, 3, 4, 4, 4, 5)

contador = 0
for numero in numeros:
    if numero == 4:
        contador += 1

print("El número 4 aparece", contador, "veces en la tupla.")