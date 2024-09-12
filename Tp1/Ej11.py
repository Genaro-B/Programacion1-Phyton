#Enunciado:11) Escribe una aplicación con una variable que contenga una contraseña cualquiera. 
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya 
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”. 
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden 
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se 
#ha bloqueado después de los 3 intentos”. Fin programa.

#Creamos la variable clave y la inicializamos:
clave="Admin12"
ingreso=""
intentos=3
#Creamos un bucle while que nos permita repetir el proceso en caso de un fallo(contraseña incorrecta)
while(ingreso!=clave and intentos>0):
    ingreso=input("Ingrese su contraseña:")
    intentos-=1

if(intentos==0 and ingreso!=clave):
    print("El acceso se ha bloqueado despues de los 3 intentos.")
else:
    print("Acceso correcto.")

print("--Fin programa--")