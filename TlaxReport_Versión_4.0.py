#Proyecto TlaxReport
#Versión 4.0
contador = 0

nombre = [""] * 100
direc = [""] * 100
descrip = [""] * 100
tipoDenuncia = [""] * 100

while True:

    print("\n===== TLAXREPORT =====")
    print("Sistema de Registro de Denuncias Ciudadanas")
    print("1. Hacer una denuncia")
    print("2. Mostrar todas las denuncias")
    print("3. Buscar denuncia por nombre")
    print("4. Buscar denuncia por tipo")
    print("5. Salir")

    opc = int(input("Seleccione una opción: "))

    if opc == 1:

        print("\n===== TIPOS DE DENUNCIA =====")
        print("1. Baches")
        print("2. Alumbrado público")
        print("3. Fuga de agua")
        print("4. Semáforos")
        print("5. Fuga de gas")

        tipo = int(input("Seleccione una opción: "))

        if tipo == 1:

            contador += 1

            tipoDenuncia[contador] = "Baches"

            print("\n===== REPORTE DE BACHES =====")

            nombre[contador] = input("Ingrese su nombre completo: ")
            direc[contador] = input("Ingrese la dirección: ")
            descrip[contador] = input("Describa el problema: ")

            print("Tu reporte ha sido guardado correctamente")

        elif tipo == 2:

            print("\n===== REPORTE DE ALUMBRADO PUBLICO =====")
            print("1. Falta de Alumbrado")
            print("2. Mantenimiento de Alumbrado")

            subopc = int(input("Seleccione una opción: "))

            contador += 1

            if subopc == 1:

                tipoDenuncia[contador] = "Falta de Alumbrado"

            elif subopc == 2:

                tipoDenuncia[contador] = "Mantenimiento de Alumbrado"

            else:

                print("Opción no válida")
                contador -= 1
                continue

            nombre[contador] = input("Ingrese su nombre completo: ")
            direc[contador] = input("Ingrese la dirección: ")
            descrip[contador] = input("Describa el problema: ")

            print("Tu reporte ha sido guardado correctamente")

        elif tipo == 3:

            contador += 1

            tipoDenuncia[contador] = "Fuga de agua"

            print("\n===== REPORTE DE FUGA DE AGUA =====")

            nombre[contador] = input("Ingrese su nombre completo: ")
            direc[contador] = input("Ingrese la dirección: ")
            descrip[contador] = input("Describa el problema: ")

            print("Tu reporte ha sido guardado correctamente")

        elif tipo == 4:

            print("\n===== REPORTE DE SEMAFOROS =====")
            print("1. Faltan Semáforos")
            print("2. Mantenimiento de Semáforos")

            subopc = int(input("Seleccione una opción: "))

            contador += 1

            if subopc == 1:

                tipoDenuncia[contador] = "Faltan Semáforos"

            elif subopc == 2:

                tipoDenuncia[contador] = "Mantenimiento de Semáforos"

            else:

                print("Opción no válida")
                contador -= 1
                continue

            nombre[contador] = input("Ingrese su nombre completo: ")
            direc[contador] = input("Ingrese la dirección: ")
            descrip[contador] = input("Describa el problema: ")

            print("Tu reporte ha sido guardado correctamente")

        elif tipo == 5:

            contador += 1

            tipoDenuncia[contador] = "Fuga de gas"

            print("\n===== REPORTE DE FUGA DE GAS =====")

            nombre[contador] = input("Ingrese su nombre completo: ")
            direc[contador] = input("Ingrese la dirección: ")
            descrip[contador] = input("Describa el problema: ")

            print("Tu reporte ha sido guardado correctamente")

        else:

            print("Opción no válida")

    elif opc == 2:

        if contador == 0:

            print("\nNo hay denuncias registradas")

        else:

            print("\n===== LISTA DE DENUNCIAS =====")

            for i in range(1, contador + 1):

                print("\nDenuncia", i)
                print("Nombre:", nombre[i])
                print("Dirección:", direc[i])
                print("Descripción:", descrip[i])
                print("Tipo:", tipoDenuncia[i])

    elif opc == 3:

        encontrado = False

        buscarNombre = input("Ingrese el nombre a buscar: ")

        for i in range(1, contador + 1):

            if nombre[i].lower() == buscarNombre.lower():

                encontrado = True

                print("\n===== DENUNCIA ENCONTRADA =====")
                print("Nombre:", nombre[i])
                print("Dirección:", direc[i])
                print("Descripción:", descrip[i])
                print("Tipo:", tipoDenuncia[i])

        if encontrado == False:

            print("No se encontró ninguna denuncia")

    elif opc == 4:

        encontrado = False

        print("\n===== BUSCAR POR TIPO =====")
        print("1. Baches")
        print("2. Falta de Alumbrado")
        print("3. Mantenimiento de Alumbrado")
        print("4. Fuga de agua")
        print("5. Faltan Semáforos")
        print("6. Mantenimiento de Semáforos")
        print("7. Fuga de gas")

        buscartipo = int(input("Seleccione una opción: "))

        if buscartipo == 1:

            tipoabuscar = "Baches"

        elif buscartipo == 2:

            tipoabuscar = "Falta de Alumbrado"

        elif buscartipo == 3:

            tipoabuscar = "Mantenimiento de Alumbrado"

        elif buscartipo == 4:

            tipoabuscar = "Fuga de agua"

        elif buscartipo == 5:

            tipoabuscar = "Faltan Semáforos"

        elif buscartipo == 6:

            tipoabuscar = "Mantenimiento de Semáforos"

        elif buscartipo == 7:

            tipoabuscar = "Fuga de gas"

        else:

            print("Opción no válida")
            continue

        for i in range(1, contador + 1):

            if tipoDenuncia[i] == tipoabuscar:

                encontrado = True

                print("\n===== DENUNCIA ENCONTRADA =====")
                print("Nombre:", nombre[i])
                print("Dirección:", direc[i])
                print("Descripción:", descrip[i])
                print("Tipo:", tipoDenuncia[i])

        if encontrado == False:

            print("No se encontraron denuncias de ese tipo")

    elif opc == 5:

        print("Saliendo del sistema...")
        break

    else:

        print("Opción no válida")
