#Esta es la version del ejercicio 12 pero con otro estilo de switch case 
dia_de_semana=0
while(dia_de_semana<1 or dia_de_semana>7):
    dia_de_semana=int(input("Ingrese un día de la semana (1-7):"))
    match dia_de_semana:
        case 1:
          print("Lunes:Día laboral")
        case 2:
            print("Martes:Día laboral")
        case 3:
            print("Miercoles:Día laboral")
        case 4:
            print("Jueves:Día laboral")
        case 5:
            print("Viernes:Día laboral")
        case 6:
            print("Sabado:Día no laboral")
        case 7:
            print("Domindo:Día no laboral")
        case _:
            print("--Día no existente--")


