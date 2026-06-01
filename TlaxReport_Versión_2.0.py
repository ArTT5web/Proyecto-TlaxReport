#Proyecto TlaxReport
#Versión 2.0
contador = 0

nombre = [""] * 100
direc = [""] * 100
descrip = [""] * 100
tipoDenuncia = [""] * 100

while True:

    print("\n===== TlaxReport =====")
    print("1. Baches")
    print("2. Alumbrado público")
    print("3. Fuga de agua")
    print("4. Semáforos")
    print("5. Fuga de gas")
    print("6. Mostrar todas las denuncias")
    print("7. Buscar denuncia por nombre")
    print("8. Buscar denuncia por tipo")
    print("9. Salir")

    opc = int(input("Seleccione una opción: "))

    if opc == 1:

        contador += 1
        tipoDenuncia[contador] = "Baches"

        nombre[contador] = input("Ingrese su nombre: ")
        direc[contador] = input("Ingrese la dirección: ")
        descrip[contador] = input("Describa el problema: ")

        print("Reporte guardado")

    elif opc == 2:

        print("1. Falta de Alumbrado")
        print("2. Mantenimiento de Alumbrado")

        subopc = int(input("Seleccione: "))

        contador += 1

        if subopc == 1:
            tipoDenuncia[contador] = "Falta de Alumbrado"
        else:
            tipoDenuncia[contador] = "Mantenimiento de Alumbrado"

        nombre[contador] = input("Ingrese su nombre: ")
        direc[contador] = input("Ingrese la dirección: ")
        descrip[contador] = input("Describa el problema: ")

        print("Reporte guardado")

    elif opc == 3:

        contador += 1
        tipoDenuncia[contador] = "Fuga de agua"

        nombre[contador] = input("Ingrese su nombre: ")
        direc[contador] = input("Ingrese la dirección: ")
        descrip[contador] = input("Describa el problema: ")

        print("Reporte guardado")

    elif opc == 4:

        print("1. Faltan Semáforos")
        print("2. Mantenimiento de Semáforos")

        subopc = int(input("Seleccione: "))

        contador += 1

        if subopc == 1:
            tipoDenuncia[contador] = "Faltan Semáforos"
        else:
            tipoDenuncia[contador] = "Mantenimiento de Semáforos"

        nombre[contador] = input("Ingrese su nombre: ")
        direc[contador] = input("Ingrese la dirección: ")
        descrip[contador] = input("Describa el problema: ")

        print("Reporte guardado")

    elif opc == 5:

        contador += 1
        tipoDenuncia[contador] = "Fuga de gas"

        nombre[contador] = input("Ingrese su nombre: ")
        direc[contador] = input("Ingrese la dirección: ")
        descrip[contador] = input("Describa el problema: ")

        print("Reporte guardado")

    elif opc == 6:

        for i in range(1, contador + 1):

            print("\nDenuncia", i)
            print("Nombre:", nombre[i])
            print("Dirección:", direc[i])
            print("Descripción:", descrip[i])
            
    elif opc == 7:

        encontrado = False

        buscarNombre = input("Nombre a buscar: ")

        for i in range(1, contador + 1):
            if nombre[i] == buscarNombre:

                encontrado = True

                print("Denuncia Encontrada")
                print(nombre[i])
                print(direc[i])
                print(descrip[i])

                break
        if encontrado == False:
            print("No se encontró ninguna denuncia")

    elif opc == 8:
        
        encontrado = False

        tipoabuscar = input("Tipo a buscar: ")

        for i in range(1, contador + 1):
            if tipoDenuncia[i] == tipoabuscar:

                encontrado = True
                
                print("Denuncia encontrada")
                print(nombre[i])

                break
        if encontrado == False:
            print("No se encontraron denuncias")
            
    elif opc == 9:
        
        print("Saliendo del sistema...")

        break
