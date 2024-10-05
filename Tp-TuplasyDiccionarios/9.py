texto = "manzana naranja manzana pera pera pera naranja manzana"

diccionario_palabras = {}

palabras = texto.split()

for palabra in palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1

print(diccionario_palabras)