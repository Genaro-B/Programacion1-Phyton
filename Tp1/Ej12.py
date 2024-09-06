#Enunciado:12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia 
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida 
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor 
#nuevamente. 

#Creamos la variable día de semana:
dia_de_semana=0
#Bucle while para repetir en caso de que el dia no exista.
while(dia_de_semana<1 or dia_de_semana>7):
    dia_de_semana=int(input("Ingrese un día de la semana:"))
    if(dia_de_semana==1):
        print("Lunes:Día laboral")
    elif(dia_de_semana==2):
        print("Martes:Día laboral")
    elif(dia_de_semana==3):
        print("Miercoles:Día laboral")
    elif(dia_de_semana==4):
        print("Jueves:Día laboral")
    elif(dia_de_semana==5):
        print("Viernes:Día laboral")
    elif(dia_de_semana==6):
        print("Sabado:Día no laboral")
    elif(dia_de_semana==7):
        print("Domingo:Día no laboral")
    else:
        print("---ERROR(Día no existente)---")