
try: 
    numero_dia = int(input("ingrese un numero del 1 al 7: "))

    match numero_dia:
        case 1:
            print("El día seleccionado es: Lunes")

        # Completa los casos del 2 al 7.
    
        case 2:
            print("El dia seleccionado es: Martes")

        case 3:
            print("El dia seleccionado es: Miercoles")


        case 4:
            print("El dia seleccionado es: Jueves")

        case 5:
            print("El dia seleccionado es: Viernes")

        case 6:
            print("El dia seleccionado es: Sabado")

        case 7:
            print("El dia seleccionado es: Domingo")

    
        case _:
            print("Error: el número debe estar entre 1 y 7.")

            print("")

except ValueError:
  print("Debes ingresarun numero valido")